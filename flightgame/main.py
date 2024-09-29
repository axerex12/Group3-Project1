from flightgame.db.Database import Database
import flightgame.flying.flying as fl

database = Database()
while True:
    fl.fly_menu(database, distance=500, user="heini")
