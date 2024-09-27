import mysql.connector
import json
from geopy import distance

'''
get a list of airports that are close
select an airport to fly to
    random events
calculate mileage and see if the flight completed
get an another list of airports
...

if at a right airport for a contract deliver the contract
'''


def load_db():
    with open("./db.json") as file:
        database = json.load(file)
    connection = mysql.connector.connect(
        host=database["host"],
        port=database["port"],
        database=database["database"],
        username=database["username"],
        password=database["password"],
        autocommit=True,
    )
    return connection


cxc = load_db()


def calculate_distance(current: tuple, destination: tuple):
    return distance.distance(current, destination)


def get_airport_by_distance(current: tuple, distance):
    sql = """
        select ident as icao, latitude_deg, longitude_deg 
        from airport
        where type = "large_airport"
    """

    airports_near = []

    with cxc.cursor(dictionary=True) as cursor:
        cursor.execute(sql, )
        data = cursor.fetchall()
        for row in data:
            airport_location = (row["latitude_deg"], row["longitude_deg"])
            if calculate_distance(current, airport_location) < distance:
                airports_near.append(row["icao"])
    return airports_near


airports = get_airport_by_distance((20, 50), 1000)
print(airports[:])


def fly_menu():
    print()


def calculate_mileage():
    print()


def fly_to():
    print()
