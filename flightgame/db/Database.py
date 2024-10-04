from locale import currency

import mysql.connector
import json
import os

class Database:

    def __init__(self):
        current_dir = os.path.dirname(__file__)
        db_path = os.path.join(current_dir, '..', '..', 'db.json')
        with open(db_path) as file:
            database = json.load(file)
        self.connection = mysql.connector.connect(
            host=database["host"],
            port=database["port"],
            database=database["database"],
            username=database["username"],
            password=database["password"],
            autocommit=True,
            buffered=True,
        )
        self.cursor = self.connection.cursor(dictionary=True)
        self.validate_database()

    def validate_database(self):
        cursor = self.cursor
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS country (
                iso_country VARCHAR(40) PRIMARY KEY,
                name VARCHAR(40),
                continent VARCHAR(40),
                wikipedia_link VARCHAR(40),
                keywords VARCHAR(40)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS airport (
                id INT(11) PRIMARY KEY,
                ident VARCHAR(40),
                type VARCHAR(40),
                name VARCHAR(40),
                latitude_deg DOUBLE,
                longitude_deg DOUBLE,
                elevation_ft INT(11),
                continent VARCHAR(40),
                iso_country VARCHAR(40),
                iso_region VARCHAR(40),
                municipality VARCHAR(40),
                scheduled_service VARCHAR(40),
                gps_code VARCHAR(40),
                iata_code VARCHAR(40),
                local_code VARCHAR(40),
                home_link VARCHAR(40),
                wikipedia_link VARCHAR(40),
                keywords VARCHAR(40),
                FOREIGN KEY (iso_country) REFERENCES country(iso_country)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS plane (
                id INT(8),
                type VARCHAR(40),
                fuel_consumption INT(32),
                max_speed INT(16),
                PRIMARY KEY (id)
            );
        """)
        cursor.execute("""
            ALTER TABLE game 
                ADD COLUMN IF NOT EXISTS (currency INT(32),
                rented_plane INT(8),
                fuel_amount INT (8),
                current_day INT (8),
                FOREIGN KEY (rented_plane) REFERENCES plane(id))
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cargo (
                id INT(8),
                delivery_value INT(16),
                weight INT(16),
                description TEXT,
                PRIMARY KEY (id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cargo_list (
                game_id INT(11),
                cargo_id INT(8),
                PRIMARY KEY (game_id, cargo_id)
            );
        """)

    def get_current_airport(self, user):
        """
        Hakee nykyisen lentokentän tiedot käyttäjän mukaan.

        :param user: Käyttäjänimi.
        :return: Nykyisen lentokentän tiedot sanakirjana tai None, jos ei löydy.
        """
        sql_fetch_current_airport = f"""
            SELECT name, ident, latitude_deg, longitude_deg
            FROM airport
            INNER JOIN game ON location = ident
            WHERE screen_name = "{user}"
        """
        self.cursor.execute(sql_fetch_current_airport)
        result = self.cursor.fetchone()
        return result if result else None

    def get_airport(self, icao: str) -> dict:
        """
        Fetch airport from database by icao
        :param icao:
        :return airport:
        """
        self.cursor.execute(f"SELECT * FROM airport WHERE ident='{icao}'")
        return self.cursor.fetchall()[0]

    def get_random_airport(self, amount: int) -> list:
        self.cursor.execute(f"SELECT * FROM airport ORDER BY RAND() LIMIT {amount}")
        return self.cursor.fetchall()

    def get_airports_by_iso(self, iso: str) -> list:
        """
        Fetch all airport from country by country's iso code
        :param iso:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM airport WHERE iso_country='{iso}'")
        return self.cursor.fetchall()

    def get_airports_by_distance(self, airport_type: str, distance: int, user: str, limit: int) -> list:
        """
        get all airports from the database that are inside certain radius from user's current loc
        :param airport_type: limit what size of airports we are interested in
        :param distance: radius that we use to look for new airports
        :param user: screen_name of an user
        :return:
        """

        current_airport = self.get_current_airport(user)

        # some sql voodoo to get all airports in a radius
        sql_get_airports_in_distance = f"""
            SELECT country.name as country, airport.name as airport, ident, latitude_deg, longitude_deg,
                (6371 * acos(
                        cos(radians({current_airport["latitude_deg"]})) * cos(radians(latitude_deg)) *
                        cos(radians(longitude_deg) - radians({current_airport["longitude_deg"]})) +
                        sin(radians(
                            {current_airport["latitude_deg"]})) * sin(radians(latitude_deg))
                )) AS distance
            FROM airport
            inner join country on country.iso_country = airport.iso_country
            WHERE airport.type = "{airport_type}"
            HAVING distance <= {distance} AND distance > 1
            ORDER BY distance
            LIMIT {limit};
        """

        self.cursor.execute(sql_get_airports_in_distance)
        return self.cursor.fetchall()

    def get_current_airport(self, user: str) -> dict:
        sql_fetch_current_airport = f"""
                    select name, ident, latitude_deg, longitude_deg
                    from airport
                    inner join game on location = ident
                    where screen_name = "{user}"
                """
        self.cursor.execute(sql_fetch_current_airport)
        return self.cursor.fetchone()

    def get_airport_by_coords(self, lat, lon, tolerance=1):
        """
        Get an airport by coordinates within a certain tolerance.

        :param lat: Latitude
        :param lon: Longitude
        :param tolerance: Degree of tolerance for latitude/longitude comparison (default 1)
        :return: The matching airport record or None
        """
        sql = f"""
            SELECT * FROM airport 
            WHERE (latitude_deg BETWEEN {lat - tolerance} AND {lat + tolerance})
            AND (longitude_deg BETWEEN {lon - tolerance} AND {lon + tolerance})
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        if result is None:
            print(f"No airport found near coordinates ({lat}, {lon})")
        return result

    def get_cargo(self, cargo_id: int) -> dict:
        self.cursor.execute(f"SELECT * FROM cargo WHERE id={cargo_id}")
        return self.cursor.fetchone()

    def get_random_cargo(self, amount: int) -> list:
        self.cursor.execute(f"SELECT * FROM cargo ORDER BY RAND() LIMIT {amount}")
        return self.cursor.fetchall()

    def get_cargo_in_game(self, game_id: int) -> list:
        self.cursor.execute(f"""SELECT cargo_id 
                                FROM cargo_list 
                                WHERE game_id={game_id}
                            """)
        return self.cursor.fetchall()
    
    def assign_cargo(self, cargo_id, user):
        """
        assign_cargo to user by its id
        :param user: screen_name of an user
        :return:
        """
        sql_assign_cargo = f"""
            INSERT INTO cargo_list (game_id, cargo_id)
            VALUES (
                (SELECT id FROM game WHERE screen_name = "{user}"),
                (SELECT id FROM cargo WHERE id = {cargo_id})
            )
        """
        self.cursor.execute(sql_assign_cargo)
    
    def remove_cargo(self, user) -> int:
        """
        remove ALL cargo from user by screen_name
        :param user: screen_name of an user
        :return:
        """
        sql_remove_cargo = f"""
            delete from cargo_list
            where game_id = (
                select id
                from game
                where screen_name = "%s"
                LIMIT = 1
            )
        """
        self.cursor.execute(sql_remove_cargo, user)

    def get_plane(self, user) -> dict:
        """
        get the current plane user is flying from the database
        :param user: screen_name of an user
        :return:
        """
        sql_get_plane = f"""
        SELECT *
        FROM plane
        WHERE id = (
            SELECT rented_plane
            FROM game
            WHERE screen_name = "{user}"
        )
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

    def update_data(self, data: list, table: str, id_column="id"):
        """
        update data in a table, the data needs to be in the same format
        :param data: list of dictionaries, where each dictionary is a row
        :param table: name of the table
        :param id_column: name of the field we use to narrow down
        :return:
        """

        for item in data:
            # Extract columns and values from the dictionary
            columns = [f"{key} = %s" for key in item if key != id_column]
            values = [item[key] for key in item if key != id_column]
            id_value = item[id_column]

            # Prepare the SQL update query
            sql = f"UPDATE {table} SET {', '.join(columns)} WHERE {id_column} = %s"
            values.append(id_value)
            self.cursor.execute(sql, values)
    
    def update_fuel_amount(self, fuel_amount, operator, user) -> None:
        """
        update the fuel amount
        :param fuel_amount: amount of fuel to be added or subtracted
        :operator: "+" or "-" to subtract or add
        :user: screen_name of the user
        """
        sql_update_fuel_amount = f"""
                UPDATE game
                SET fuel_amount = fuel_amount {operator} {fuel_amount}
                WHERE screen_name = "{user}"
            """
        if fuel_amount > 0 and (operator == "+" or operator == "-"):
            self.cursor.execute(sql_update_fuel_amount)
        else:
            return Exception("Incorrect operator or fuel amount")
        return "fuel updated"

    def add_time(self, amount_min, user):
        sql = f"UPDATE game SET current_day=current_day+{amount_min/3600} WHERE screen_name='{user}'"
        self.cursor.execute(sql)


    def update_currency_amount(self, currency, operator, user):
        """
        update the currency amount
        """
        sql_update_currency_amount = f"""
                UPDATE game
                SET currency = currency {operator} {currency}
                WHERE screen_name = "{user}"
            """
        self.cursor.execute(sql_update_currency_amount)