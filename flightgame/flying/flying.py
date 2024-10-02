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

class Flying:
    def __init__(self) -> None:
        self.db = Database()
        self.time_minutes = 0

    def fly_menu(self, airport_type, distance, user):
        # encounter = encounters.Encounter()

        airports_near = self.db.get_airports_by_distance(
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
                self.fly_to(self.db, selected_airport, user)

                # encounter tähän väliin tai fly_to mukaan
                if rd.randint(0, 6) == 6:
                    print("ENCOUNTER")


                # id INT(8),
                # type VARCHAR(40),
                # fuel_consumption INT(32),
                # max_speed INT(16),
                # PRIMARY KEY (id)

                self.time_minutes += self.db.get_plane(user)["max_speed"] * selected_airport["distance"]
                    
                # fly_to olis varmaan parempi koti tälle
                # update spent fuel // currently it just puts the amount of spend fuel as fuel_amount
                self.db.update_fuel_amount(self.calculate_spent_fuel(selected_airport["distance"], user), "-", user)
            except Exception as exc:
                print(exc)
                continue
            running = False


    def fly_to(self, airport: dict, user: str):
        # need to make some kind of class to keep track of what user we are on
        print(f"\nFlying to |{airport['ident']}| |{ airport['airport']}| in |{airport['country']}\n")
        self.db.update_data( [{"location": airport["ident"], "screen_name": user}], "game", "screen_name")


    def get_midpoint(self, origin: tuple, destination: tuple) -> tuple[float, float]:
        """
        returns midpoint of twoo coordinates
        :param origin: origin point
        :param destinatio: destination point
        :return:
        """
        x: float = (origin[0] + destination[0]) / 2
        y: float = (origin[1] + destination[1]) / 2
        print("midpoint")
        return (x, y)

    def calculate_spent_fuel(self, distance, user) -> int:
        plane: dict = self.db.get_plane(user)
        # return used fuel based on L/100km
        return int(plane["fuel_consumption"] * distance / 100)

if __name__ == "__main__":
    print("Running!")
    flying = Flying()
    print(flying.get_midpoint((51.5072, 0.1276), (60.1699, 24.9384)))

