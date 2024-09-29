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


def fly_menu(database: Database, distance, user):
    airports_near = database.get_airports_by_distance(
        "large_airport", distance, user)

    # list all nearby airports, make the user use numbers from 1
    # while selecting the airport since that is more natural
    for airport in airports_near:
        print(f"Fly to |{airport["airport"]}| in |{airport["country"]}| distance(you) {airport["distance"]:.0f} by selecting ({
              airports_near.index(airport) + 1})")

    # TODO: bug: allows using negative numbers

    running = True
    while running:
        try:
            user_input = int(input("Selection: ")) - 1
            if user_input + 1 <= 0:
                continue
            fly_to(database, airports_near[user_input], user)
        except Exception as exc:
            print(exc)
            continue
        running = False


def fly_to(database: Database, airport: dict, user: str):
    # need to make some kind of class to keep track of what user we are on
    print(f"\nFlying to |{airport["ident"]}| |{
          airport['airport']}| in |{airport['country']}\n")
    database.update_location(airport["ident"], user)


def calculate_mileage(distance, plane):
    return plane.fuel_usage * distance


if __name__ == "__main__":
    print("Running!")
