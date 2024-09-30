import mysql.connector
import json

class Database:

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
                fuel_amount int (8),
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

    def add_data(self, data: list, table: str):
        """
        Add data to a table, the data needs to be in the same format
        :param data: list of dictionaries, where each dictionary is a row
        :param table: name of the table
        :return:
        """
        for item in data:
            columns = ','.join([str(name) for name, val in item.items()])
            values = ','.join([f"'{val}'" if isinstance(val, str) else str(val) for name, val in item.items()])
            statement = f"INSERT IGNORE INTO {table} ({columns}) VALUES ({values});"
            print(statement)
            self.cursor.execute(statement)
