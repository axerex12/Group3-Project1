from tracemalloc import Traceback

from flightgame.db.Database import Database
from flightgame.flying import encounters
import random as rd
import traceback

from flightgame.flying.encounters import EncounterClient

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
        self.encounter_client = EncounterClient()
        self.refill_amount = 0

    def fly_menu(self, airport_type, distance, user):
        # encounter = encounters.Encounter()

        running = True
        while running:
            airports_near = self.db.get_airports_by_distance(
                airport_type, distance, user,5)

            # list all nearby airports, make the user use numbers from 1
            # while selecting the airport since that is more natural
            fuel_refill_list = []

            for airport in airports_near:
            # give random amount of fuel to refill at airports
                fuel_refill_amount = rd.randint(200,1000)
                fuel_refill_list.append(fuel_refill_amount)
                print(f"Fly to and refill fuel ({fuel_refill_amount}) at|{airport['airport']}| in |{airport['country']}| {airport['distance']:.0f} km by selecting ({airports_near.index(airport) + 1})")

            try:
                user_input = int(input("Selection: ")) - 1
                if user_input + 1 <= 0:
                    raise Exception("Selection less or equal to zero!")
                airport = selected_airport = airports_near[user_input]
                print(f"\nFlying to |{selected_airport['ident']}| |{selected_airport['airport']}| in |{selected_airport['country']}\n")
                selected_airport = airports_near[user_input]
                self.refill_amount = fuel_refill_list[user_input]
                # travel to the selected airport
                #self.fly_to(selected_airport, user)

                # encounter tähän väliin tai fly_to mukaan
                if rd.randint(0, 6) == 6:
                    print("ENCOUNTER")
                    player_airport = self.db.get_current_airport(user)
                    start_coords = (player_airport["latitude_deg"], player_airport["longitude_deg"])
                    #print(start_coords)
                    end_coords = (selected_airport["latitude_deg"], selected_airport["longitude_deg"])
                    #print(end_coords)
                    enc = self.encounter_client.random_encounter().start_encounter()
                    midpoint = self.get_midpoint(start_coords, end_coords)
                    airport = self.db.get_airport_by_coords(midpoint[0],midpoint[1])
                    if not self.handle_encounter(enc, midpoint, user):
                        break

                # id INT(8),
                # type VARCHAR(40),
                # fuel_consumption INT(32),
                # max_speed INT(16),
                # PRIMARY KEY (id)

                self.time_minutes += (self.db.get_plane(user)["max_speed"] * selected_airport["distance"])/60
                    
                # fly_to olis varmaan parempi koti tälle
                # update spent fuel // currently it just puts the amount of spend fuel as fuel_amount
                # travel to the selected airport
                #self.fly_to(selected_airport, user)
                self.land(airport,user)
                self.db.update_fuel_amount(self.calculate_spent_fuel(selected_airport["distance"], user), "-", user)
                input("continue? y/n")
            except Exception as e:
                traceback.print_exc()
                #continue
        print("Ended flying")
        running = False

    def fly_to(self, airport: dict, user: str):

        # need to make some kind of class to keep track of what user we are on
        #print(f"\nFlying to |{airport['ident']}| |{airport['airport']}| in |{airport['country']}\n")

        self.db.update_data( [{"location": airport["ident"], "screen_name": user}], "game", "screen_name")

    def get_midpoint(self, origin: tuple, destination: tuple) -> tuple[float, float]:
        """
        returns midpoint of twoo coordinates
        :param self:
        :param origin: origin point
        :param destination: destination point
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

    def land(self, airport: dict,user):
        #print(airport)
        print(f"Landed in {airport['ident']} with time {round(self.time_minutes)}")
        self.db.update_data([{"location": airport["ident"], "screen_name": user}], "game", "screen_name")

    def handle_encounter(self, enc_data: tuple, coords: tuple,user) -> bool:
        """
        handles encounter data and decides actions
        :param self:
        :param enc_data: encounter data provided by EncounterClient
        :param coords: coordinates as tuple
        :param user: username
        :return: boolean whether player continued to intended destination
        """
        success = enc_data[0]
        time_added = enc_data[1]
        action = enc_data[2]
        if success:
            #print(enc_data)
            #print(coords)
            if action== "Land":
                airport = self.db.get_airport_by_coords(coords[0], coords[1])
                self.land(airport,user)
                self.time_minutes += time_added
                #TODO: update db to accept floats in current_day
                self.db.add_time(time_added, user)
                return False
            elif action=="Wait":
                print(f"You wait for {time_added} min")
                self.time_minutes += time_added
                return True
            elif action=="Continue":
                print("You continue as normal and everything goes well")
                return True
        else:
            print("HAH! You died")
            return False

if __name__ == "__main__":
    print("Running!")
    #print(flying.get_midpoint((51.5072, 0.1276), (60.1699, 24.9384)))

