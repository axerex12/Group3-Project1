from flightgame.db.Database import Database
from flightgame.flying.flying import Flying
from flightgame.flying.encounters import EncounterClient
from flightgame.flying.flying import Flying
from flightgame.rentaplane.Planerenting import Planerenting
from flightgame.data import Data # here is all of the cargo = [] etc. to declutter main.py
from flightgame.gameclient.gameclient import GameClient

enc = EncounterClient()

db = Database()
gameclient = GameClient(db)
flying = Flying(gameclient)
pr = Planerenting()

#db.add_data(Data.cargo,"cargo")
#db.add_data(Data.planes,"plane")

while True:
    print("Running!") # just because vscode is a bit special :D
    flying.fly_menu(distance=1000, airport_type="large_airport", user="Heini")
    break
# Data used here
# db.add_data(Data.cargo,"cargo")
# db.add_data(Data.planes,"plane")
# db.assign_cargo(5, "heini")