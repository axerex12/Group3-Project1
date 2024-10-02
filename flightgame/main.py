from flightgame.db.Database import Database
from flightgame.flying.flying import Flying
from flightgame.flying.encounters import EncounterClient
from flightgame.rentaplane.Planerenting import Planerenting
from flightgame.data import Data

db = Database()
enc = EncounterClient(db)
flying = Flying(db)

db = Database()
pr = Planerenting()

# Data used here
# db.add_data(Data.cargo,"cargo")
# db.add_data(Data.planes,"plane")
# db.assign_cargo(5, "heini")

while True:
    # fl.fly_menu(db, distance=500, airport_type="large_airport", user="heini")
    flying.fly_menu("large_airport", 400, "heini")
    # print(db.get_plane("heini"))
    #fl.fly_menu(db, distance=500, airport_type="large_airport", user="heini")
    # pr.renting_menu(db, user="heini")
    # print(db.get_plane("heini"))
    # break
