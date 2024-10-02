from flightgame.db.Database import Database
import flightgame.flying.flying as fl

db = Database()

while True:
    fl.fly_menu(db, "large_airport", 500, "heini")