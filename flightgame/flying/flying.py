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


def calculate_distance(current: tuple, destination: tuple):
    return distance.distance(current, destination)


# get all airports inside certain distance from current one
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


def fly_menu(current_airport, distance):
    airports_near = get_airport_by_distance(current_airport, distance)

    # list all nearby airports, make the user use numbers from 1
    # while selecting the airport since that is more natural
    for airport in airports_near:
        print(f"Fly to {airport} by selecting ({
              airports_near.index(airport) + 1})")

    # TODO: bug: allows using negative numbers
    running = True
    while running:
        try:
            user_input = int(input()) - 1
            print(f"Flying to ... {airports_near[user_input]}")
        except:
            print("Invalid input!")
            continue
        running = False

    # calculate fuel usage from plane stats


def calculate_mileage(distance, plane):
    return plane.fuel_usage * distance


def fly_to():
    print("")


if __name__ == "__main__":
    print("Running!")
    cxc = load_db()
    fly_menu((51.5072, 0.1276), 50)
    # airports = get_airport_by_distance((51.5072, 0.1276), 50)
    # print(airports[:])
