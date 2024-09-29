from flightgame.db.Database import Database
import flightgame.flying.flying as fl

database = Database()
fl.fly_menu(database, distance=500)
