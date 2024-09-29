from db.Database import Database
import flying.flying as fl


database = Database()
fl.fly_menu(database, distance=500)
