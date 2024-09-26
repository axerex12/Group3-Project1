import mysql.connector
import json
class Database:

    def __init__(self):
        with open("../db.json") as file:
             database = json.load(file)
        self.connection = mysql.connector.connect(host=database["host"],
                                             port=database["port"],
                                             database=database["database"],
                                             username=database["username"],
                                             password=database["password"],
                                             autocommit=True)
        self.cursor = self.connection.cursor(dictionary=True)


    def validate_database(self):
        expected_schema = {
            "airport":{
                "id":"int(11)",
                "ident":"varchar(40)",
                "type":"varchar(40)",
                "name":"varchar(40)",
                "latitude_deg":"double",
                "longitude_deg":"double",
                "elevation_ft":"int(11)",
                "continent":"varchar(40)",
                "iso_country":"varchar(40)",
                "iso_region":"varchar(40)",
                "municipality":"varchar(40)",
                "scheduled_service":"varchar(40)",
                "gps_code":"varchar(40)",
                "iata_code":"varchar(40)",
                "local_code":"varchar(40)",
                "home_link":"varchar(40)",
                "wikipedia_link":"varchar(40)",
                "keywords":"varchar(40)"
            },
            "country":{
                "iso_country":"varchar(40)",
                "name":"varchar(40)",
                "continent":"varchar(40)",
                "wikipedia_link":"varchar(40)",
                "keywords":"varchar(40)"
            },
            "game":{
                "id":"varchar(40)",
                "co2_consumed":"int(8)",
                "co2_budget":"int(8)",
                "location":"varchar(10)",
                "screen_name":"varchar(40)",
                "currency":"int(32)",
                "rented_plane":"int(8)"
            },
            "plane":{
                "id": "int(8)",
                "type":"varchar(40)",
                "fuel_consumption": "int(32)",
                "max_speed": "int(16)",
            },
            "cargo":{
                "id": "int(8)",
                "delivery_value":"int(16)",
                "weight":"int(16)",
                "description":"text"
            },
            "cargo_list":{
                "game_id":"int(11)",
                "cargo_id":"int(8)"
            }
        }
        print(expected_schema)

    def get_current_schema(self):
        """Get current schema from the database."""
        cursor = self.cursor
        schema = {}

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for row in tables:
            table_name = row["Tables_in_flight_game_project"]
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            schema[table_name] = {col["Field"]: col["Type"] for col in columns}

        return schema

    def get_airport(self,icao: str) -> dict:
        """
        Fetch airport from database by icao
        :param icao:
        :return airport:
        """
        self.cursor.execute(f"SELECT * FROM airport WHERE ident='{icao}'")
        return self.cursor.fetchall()[0]

    def get_airports_by_iso(self,iso: str) -> list:
        """
        Fetch all airport from country by country's iso code
        :param iso:
        :return:
        """
        self.cursor.execute(f"SELECT * FROM airport WHERE iso_country='{iso}'")
        return self.cursor.fetchall()

