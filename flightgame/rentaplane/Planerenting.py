from flightgame.db.Database import Database

class Planerenting:
    # valitsee randomin lentokoneen
    def plane_chooser(self, db: Database, amount: int) -> list:
        x = 0
        random_planes = db.get_random_plane(amount)
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

    def renting_menu(self, db: Database):
        print("Welcome to plane-to-succeed rental! Here's our current selection:")
        max_planes = 3
        planes = self.plane_chooser(db, max_planes)
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
                if (userInput <= 0) and (userInput > max_planes):
                    print("Not a valid index! Try again!")
                    continue
                else:
                    print(planes[userInput - 1])  # Just shows what was chosen for now
                    break