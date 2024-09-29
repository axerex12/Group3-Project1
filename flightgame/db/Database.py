import mysql.connector
import json


class Database:

    EXPECTED_SCHEMA = {
        "airport": {
            "id": "int(11)",
            "ident": "varchar(40)",
            "type": "varchar(40)",
            "name": "varchar(40)",
            "latitude_deg": "double",
            "longitude_deg": "double",
            "elevation_ft": "int(11)",
            "continent": "varchar(40)",
            "iso_country": "varchar(40)",
            "iso_region": "varchar(40)",
            "municipality": "varchar(40)",
            "scheduled_service": "varchar(40)",
            "gps_code": "varchar(40)",
            "iata_code": "varchar(40)",
            "local_code": "varchar(40)",
            "home_link": "varchar(40)",
            "wikipedia_link": "varchar(40)",
            "keywords": "varchar(40)",
        },
        "country": {
            "iso_country": "varchar(40)",
            "name": "varchar(40)",
            "continent": "varchar(40)",
            "wikipedia_link": "varchar(40)",
            "keywords": "varchar(40)",
        },
        "game": {
            "id": "int(11)",
            "co2_consumed": "int(8)",
            "co2_budget": "int(8)",
            "location": "varchar(10)",
            "screen_name": "varchar(40)",
            "currency": "int(32)",
            "rented_plane": "int(8)",
        },
        "plane": {
            "id": "int(8)",
            "type": "varchar(40)",
            "fuel_consumption": "int(32)",
            "max_speed": "int(16)",
        },
        "cargo": {
            "id": "int(8)",
            "delivery_value": "int(16)",
            "weight": "int(16)",
            "description": "text",
        },
        "cargo_list": {
            "game_id": "int(11)",
            "cargo_id": "int(8)"},
    }

    def __init__(self):
        with open("../db.json") as file:
            database = json.load(file)
        self.connection = mysql.connector.connect(
            host=database["host"],
            port=database["port"],
            database=database["database"],
            username=database["username"],
            password=database["password"],
            autocommit=True,
        )
        self.cursor = self.connection.cursor(dictionary=True)
        print(self.validate_database())

    def validate_database(self) -> bool:
        current_schema = self.get_current_schema()
        if current_schema != self.EXPECTED_SCHEMA:
            alter_statements = self.generate_alter_statements()
            for statement in alter_statements:
                print(f"Executing: {statement}")
                self.cursor.execute(statement)
            return False
        return True

    def generate_alter_statements(self):
        """
        Generates the statements needed for changing database
        :return:
        """
        alter_statements = []
        original = self.get_current_schema()
        print(f"Original: {original}")
        updated = self.EXPECTED_SCHEMA
        print(f"Expected: {updated}")
        for table, fields in updated.items():
            print(fields.items())

            if table not in original:
                columns = ", ".join(
                    [f"{col} {data_type}" for col,
                        data_type in fields.items()]
                )
                create_table = f"CREATE TABLE {table} ({columns})"
                alter_statements.append(create_table)
            else:
                original_fields = original[table]
                for col, data_type in fields.items():
                    if col not in original_fields:
                        alter_statements.append(
                            f"ALTER TABLE {table} ADD COLUMN {col} {data_type}"
                        )
                    elif original_fields[col] != data_type:
                        alter_statements.append(
                            f"ALTER TABLE {table} MODIFY COLUMN {
                                col} {data_type}"
                        )
        return alter_statements

    def get_current_schema(self) -> dict:
        """Get current schema from the database."""
        cursor = self.cursor
        schema = {}

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for row in tables:
            table_name = row["Tables_in_flight_game"]
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            schema[table_name] = {
                col["Field"]: f'{col["Type"]} {col["Key"]}' for col in columns
            }

        return schema

    def get_airport(self, icao: str) -> dict:
        """
        Fetch airport from database by icao
        :param icao:
        :return airport:
        """
        self.cursor.execute(f"SELECT * FROM airport WHERE ident='{icao}'")
        return self.cursor.fetchall()[0]

    def get_airports_by_iso(self, iso: str) -> list:
        """
        Fetch all airport from country by country's iso code
        :param iso:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM airport WHERE iso_country='{iso}'")
        return self.cursor.fetchall()

    # get all airports inside certain distance from current one
    def get_airports_by_distance(self, airport_type: str, distance: int) -> list:
        # somehow we need to keep track of what id is the current game using
        sql_fetch_current_airport = f"""
            select name, ident, latitude_deg, longitude_deg
            from airport
            inner join game on location = ident
            where game.id = 1
        """

        self.cursor.execute(sql_fetch_current_airport)
        current_airport = self.cursor.fetchall()[0]

        # some sql voodoo to get all airports in a radius
        sql_get_airports_in_distance = f"""
            SELECT country.name as country, airport.name as airport, ident,
                (6371 * acos(
                        cos(radians({current_airport["latitude_deg"]})) * cos(radians(latitude_deg)) *
                        cos(radians(longitude_deg) - radians({current_airport["longitude_deg"]})) +
                        sin(radians(
                            {current_airport["latitude_deg"]})) * sin(radians(latitude_deg))
                )) AS distance
            FROM airport
            inner join country on country.iso_country = airport.iso_country
            WHERE airport.type = "{airport_type}"
            HAVING distance <= {distance} AND distance > 0
            ORDER BY distance;
        """

        self.cursor.execute(sql_get_airports_in_distance)
        return self.cursor.fetchall()

    def get_plane(self) -> dict:
        sql_get_plane = f"""
        SELECT *
        FROM plane
        """

        self.cursor.execute(sql_get_plane)
        return self.cursor.fetchall()[0]

    def add_data(self, data: list, table: str):
        """
        Add data to a table, the data needs to be in the same format
        :param data: list of dictionaries, where each dictionary is a row
        :param table: name of the table
        :return:
        """
        for item in data:
            columns = ','.join([str(name) for name, val in item.items()])
            values = ','.join([f"'{val}'" if isinstance(
                val, str) else str(val) for name, val in item.items()])
            statement = f"INSERT INTO {table} ({columns}) VALUES ({values});"
            print(statement)
            self.cursor.execute(statement)

    def update_location(self, location: str, screen_name: str):
        sql_update_location = f"""
            UPDATE game
            SET location = %s
            WHERE screen_name = %s
        """

        self.cursor.execute(sql_update_location, (location, screen_name))
