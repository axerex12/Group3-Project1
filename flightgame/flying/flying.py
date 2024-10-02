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
    def __init__(self, database: Database) -> None:
        self.db = database
        self.time_minutes = 0
        self.refill_amount = 0

    def fly_menu(self, airport_type, distance, user):
        # encounter = encounters.Encounter()

        airports_near = self.db.get_airports_by_distance(
            airport_type, distance, user)

        # list all nearby airports, make the user use numbers from 1
        # while selecting the airport since that is more natural
        fuel_refill_list = []
        for airport in airports_near:
            # give random amount of fuel to refill at airports
            fuel_refill_amount = rd.randint(200,1000)
            fuel_refill_list.append(fuel_refill_amount)
            print(f"Fly to and refill fuel ({fuel_refill_amount}) at|{airport['airport']}| in |{airport['country']}| {airport['distance']:.0f} km by selecting ({airports_near.index(airport) + 1})")

        running = True
        while running:
            try:
                user_input = int(input("Selection: ")) - 1
                if user_input + 1 <= 0:
                    raise Exception("Selection less or equal to zero!")
                selected_airport = airports_near[user_input]
                self.refill_amount = fuel_refill_list[user_input]
                # travel to the selected airport
                self.fly_to(selected_airport, user)

                # encounter tähän väliin tai fly_to mukaan
                if rd.randint(0, 6) == 6:
                    print("ENCOUNTER")

                # id INT(8),
                # type VARCHAR(40),
                # fuel_consumption INT(32),
                # max_speed INT(16),
                # PRIMARY KEY (id)

                # d/v = t calculating time spend flying
                self.time_minutes +=  selected_airport["distance"] / self.db.get_plane(user)["max_speed"] * 60
                print(f"\nTime spent flying: {self.time_minutes:.0f} minutes\n")
                    
                # fly_to olis varmaan parempi koti tälle
                self.db.update_fuel_amount(self.calculate_spent_fuel(selected_airport["distance"], user), "-", user)
                # add the fuel amount specific to the airport
                self.db.update_fuel_amount(fuel_refill_list[user_input], "+", user)
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
    print(flying.get_midpoint((51.5072, 0.1276), (60.1699, 24.9384)))

