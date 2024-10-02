from flightgame.db.Database import Database
from flightgame.flying import encounters
import random as rd

'''
get a list of airports that are close
select an airport to fly to
    random events
calculate mileage and see if the flight completed
get an another list of airports
...

if at a right airport for a contract, deliver the contract
horribly wip refactoring
'''


def fly_menu(db: Database, airport_type, distance, user):
    # encounter = encounters.Encounter()

    airports_near = db.get_airports_by_distance(
        airport_type, distance, user)

    # list all nearby airports, make the user use numbers from 1
    # while selecting the airport since that is more natural
    for airport in airports_near:
        print(f"Fly to |{airport['airport']}| in |{airport['country']}| distance(you) {airport['distance']:.0f} by selecting ({airports_near.index(airport) + 1})")

    running = True
    while running:
        try:
            user_input = int(input("Selection: ")) - 1
            if user_input + 1 <= 0:
                raise Exception("Selection less or equal to zero!")
            selected_airport = airports_near[user_input]
            # travel to the selected airport
            fly_to(db, selected_airport, user)

            # encounter tähän väliin tai fly_to mukaan
            if rd.randint(0, 6) == 6:
                print("ENCOUNTER")
                
            # fly_to olis varmaan parempi koti tälle
            # update spent fuel // currently it just puts the amount of spend fuel as fuel_amount
            db.update_fuel_amount(calculate_spent_fuel(db, selected_airport["distance"], user), "-", user)
        except Exception as exc:
            print(exc)
            continue
        running = False


def fly_to(db: Database, airport: dict, user: str):
    # need to make some kind of class to keep track of what user we are on
    print(f"\nFlying to |{airport['ident']}| |{ airport['airport']}| in |{airport['country']}\n")
    db.update_data( [{"location": airport["ident"], "screen_name": user}], "game", "screen_name")


def get_midpoint(db: Database, origin: tuple, destination: tuple) -> tuple:
    """
    returns midpoint of twoo coordinates
    :param origin: origin point
    :param destinatio: destination point
    :return:
    """
    x = (origin[0] + destination[0]) / 2
    y = (origin[1] + destination[1]) / 2
    print("midpoint")
    return (x, y)


def calculate_spent_fuel(db: Database, distance, user) -> int:
    plane: dict = db.get_plane(user)
    # return used fuel based on L/100km
    return int(plane["fuel_consumption"] * distance / 100)


if __name__ == "__main__":
    print("Running!")
    db = Database()
    print(get_midpoint(db, (51.5072, 0.1276), (60.1699, 24.9384)))
