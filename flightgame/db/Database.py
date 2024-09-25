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

    def get_airport(self,icao: str) -> dict:
        """
        Fetch airport from database by icao
        :param icao:
        :return airport:
        """
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM airport WHERE ident='{icao}'")
        return cursor.fetchall()[0]

    def get_airports_by_iso(self,iso: str) -> list:
        """
        Fetch all airport from country by country's iso code
        :param iso:
        :return:
        """
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM airport WHERE iso_country='{iso}'")
        return cursor.fetchall()

