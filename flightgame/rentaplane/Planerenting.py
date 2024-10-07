from locale import currency

from flightgame.db.Database import Database
from flightgame.gameclient.gameclient import GameClient

class Planerenting:
    # valitsee randomin lentokoneen
    def __init__(self, gc: GameClient):
        self.db = gc.db
        self.gc = gc

    def plane_chooser(self, amount: int) -> list:
        x = 0
        random_planes = self.db.get_random_plane(amount)
        while x < amount:
            plane_fc = random_planes[x]['fuel_consumption']
            plane_ms = random_planes[x]['max_speed']
            plane_price = int(plane_fc) + int(plane_ms) * 50
            random_planes[x].update({"price": plane_price})
            x += 1
        return random_planes

    def plane_format(self, random_plane: dict, order_id: int):
        print(
            f"Vehicle type: {random_plane['type']}\nFuel consumption: {random_plane['fuel_consumption']}\nMax speed: {random_plane['max_speed']}\nRenting Price weekly: {random_plane['price']}\nID: {order_id}"
            f"\n#|---|---|---|---|---|#")

    #TODO: money substraction
    def renting_menu(self):
        print("Welcome to plane-to-succeed rental! Here's our current selection:")
        max_planes = 3
        planes = self.plane_chooser(max_planes)
        i = 0
        while i < max_planes:
            self.plane_format(planes[i], i + 1)
            i += 1
        while True:
            try:
                userInput = int(input("Which plane would you like to rent? "))
            except ValueError:
                print("Not an integer! Try again!")
                continue
            else:
                if (userInput <= 0) or (userInput > max_planes):
                    print("Not a valid index! Try again!")
                    continue
                else:
                    self.gc.rented_plane = planes[userInput-1]
                    self.gc.currency = self.gc.currency - planes[userInput-1]['price']
                    self.gc.rent_amount = planes[userInput-1]['price']
                    # select the airport type based on the type of the plane
                    if (self.gc.rented_plane["type"] == "helicopter"):
                        self.gc.airport_type = "heliport"
                    else:
                        self.gc.airport_type = "large_airport"
                    break