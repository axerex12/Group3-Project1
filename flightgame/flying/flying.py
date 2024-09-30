from flightgame.db.Database import Database


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
            fly_to(db, airports_near[user_input], user)
            # update spent fuel // currently it just puts the amount of spend fuel as fuel_amount
            # db.update_data([{"fuel_amount": calculate_spent_fuel(db, airports_near[user_input]["distance"], user), "screen_name": user}], "game", "screen_name")
            db.update_fuel_amount(calculate_spent_fuel(db, airports_near[user_input]["distance"], user), "-", user)
        except Exception as exc:
            print(exc)
            continue
        running = False


def fly_to(db: Database, airport: dict, user: str):
    # need to make some kind of class to keep track of what user we are on
    print(f"\nFlying to |{airport['ident']}| |{ airport['airport']}| in |{airport['country']}\n")
    db.update_data( [{"location": airport["ident"], "screen_name": user}], "game", "screen_name")


def calculate_spent_fuel(db: Database, distance, user) -> int:
    plane: dict = db.get_plane(user)
    # return used fuel based on L/km
    print(plane)
    return int(plane["fuel_consumption"] * distance / 100)


if __name__ == "__main__":
    print("Running!")
