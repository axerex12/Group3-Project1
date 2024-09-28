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


def calculate_distance(current: tuple, destination: tuple):
    return distance.distance(current, destination)


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
