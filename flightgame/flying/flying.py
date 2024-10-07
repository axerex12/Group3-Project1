# from flightgame.db.Database import Database
from flightgame.gameclient.gameclient import GameClient
from flightgame.flying.encounters import EncounterClient
from geopy import distance
import random as rd
import traceback


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
    def __init__(self, game_client: GameClient) -> None:
        self.db = game_client.db
        self.game_client = game_client
        self.time_minutes = 0
        self.encounter_client = EncounterClient()
        self.refill_amount = 0

    def calculate_distance(self, current_airport) -> float:
        """laskee lentokenttien etäysyydet."""
        if self.game_client.current_contract == None:
            return 0
        airport2 = self.db.get_airport(self.game_client.current_contract["destination_id"])

        if current_airport is None or airport2 is None:
            raise ValueError("One or both airports could not be found.")

        ap1_cords = (current_airport['latitude_deg'], current_airport['longitude_deg'])
        ap2_cords = (airport2['latitude_deg'], airport2['longitude_deg'])

        dist = distance.distance(ap1_cords, ap2_cords).kilometers
        return dist

    def fly_menu(self, airport_type, distance):
        # encounter = encounters.Encounter()

        # save game data ok
        # get airports to fly to ok
        # select airports ok
        # fly ok
        # check encounter ok
        # check fuel ok
        # land ok
        ## check if contract fits the airport
        # refill fuel ok

        # hack to keep the current day when loading a new session
        self.time_minutes = self.game_client.current_day * 1440

        while not self.game_client.gameover:
            # save game data
            if not self.game_client.save_game_data(self.game_client.screen_name):
                return
            self.game_client.print_game_data()

            airports_near = self.db.get_airports_by_distance(airport_type, distance, self.game_client.screen_name,5)

            # list all airports
            for airport in airports_near:
                # give random amount of fuel to refill at airports
                fuel_refill_amount = rd.randint(100,300)
                airport["fuel_refill_amount"] = fuel_refill_amount
                print(f"Fly to and refill fuel ({fuel_refill_amount}) at|{airport['airport']}| in |{airport['country']}| {airport['distance']:.0f} km by selecting ({airports_near.index(airport)})")
                print(f"Distance from cargo destination {self.calculate_distance(airport):.0f} km")
            
            # select the airport to fly to
            user_input = int(input("Selection: "))
            # while (user_input <= 0 and user_input >= len(airports_near) - 1):
            #     print("invalid selection")
            #     user_input = int(input("Selection: "))
            #     user_input = int(input("Selection: ")) - 1
            
            # assign from airports_near to airport
            airport = airports_near[user_input]
            # print the airport being flown to
            print(f"\nFlying to |{airport['ident']}| |{airport['airport']}| in |{airport['country']}\n")
            # set amount of fuel to be refilled
            self.refill_amount = airport["fuel_refill_amount"]

            if rd.randint(0, 6) == 6:
                print("ENCOUNTER")
                player_airport = self.db.get_current_airport(self.game_client.screen_name)
                start_coords = (player_airport["latitude_deg"], player_airport["longitude_deg"])
                #print(start_coords)
                end_coords = (airport["latitude_deg"], airport["longitude_deg"])
                #print(end_coords)
                enc = self.encounter_client.random_encounter().start_encounter()
                midpoint = self.get_midpoint(start_coords, end_coords)
                airport = self.db.get_airport_by_coords(midpoint[0],midpoint[1])
                if not self.handle_encounter(enc, midpoint):
                    self.game_client.gameover = True
                    break
            else:
                # adding flight time to player
                self.time_minutes += airport["distance"]/self.db.get_plane(self.game_client.screen_name)["max_speed"]*60
                # land and update fuel, date, location
                self.game_client.fuel_amount -= self.calculate_spent_fuel(airport["distance"])
                # check fuel amount and quit if under 0
                if self.game_client.fuel_amount <= 0:
                    print("Fuel ran out and you crashed!")
                    self.game_client.gameover = True
                    break
                self.land(airport)

            # asking if user wants to quit
            if input("continue? y/n: ").upper() != "Y":
                print("Saving and Exiting the game.")
                self.game_client.save_game_data(self.game_client.screen_name)
                self.game_client.gameover = True

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

    def calculate_spent_fuel(self, distance) -> int:
        plane: dict = self.db.get_plane(self.game_client.screen_name)
        # return used fuel based on L/100km
        return int(plane["fuel_consumption"] * distance / 100) * 0.8

    def land(self, airport: dict):
        if airport is None:
            print("You got lost and you died")
            self.game_client.gameover = True
        #print(airport)
        print(f"Landed in {airport['ident']} with time {round(self.time_minutes)} min, refilling fuel for {self.refill_amount}")
        # update fuel amount after landing
        self.game_client.fuel_amount += self.refill_amount
        # set current location
        self.game_client.location = self.db.get_airport(airport["ident"])
        # converts time to current day by d = 24h * 60 min/h
        self.game_client.current_day = int(self.time_minutes/1440)
        # pay every landing because why not
        self.game_client.currency -= self.game_client.rent_amount
        # pay the rent every 7th day
        # if (self.game_client.current_day % 7 == 0 and self.game_client.current_day != 0) and not self.game_client.rent_paid:
        #     print("Paying rent for the plane")
        #     self.game_client.currency -= self.game_client.rent_amount
        #     self.game_client.rent_paid = True
        # if (self.game_client.current_day % 7 != 0):
            # self.game_client.rent_paid = False
        self.game_client.check_contract_delivery(self.db.get_airport(airport["ident"]))

    def handle_encounter(self, enc_data: tuple, coords: tuple) -> bool:
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
                self.land(airport)
                self.time_minutes += time_added
                #TODO: update db to accept floats in current_day
                # self.db.add_time(time_added, self.game_client.screen_name)
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
    

