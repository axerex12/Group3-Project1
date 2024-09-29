from flightgame.db.Database import Database
import flightgame.flying.flying as fl

db = Database()
while True:
    fl.fly_menu(db, distance=500, user="heini")
    print(db.get_plane("heini"))
# db.update_values([{"type": "helicopter", "id": 1}], "plane", "id")
