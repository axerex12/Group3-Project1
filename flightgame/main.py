from db.Database import Database
import flying.flying as fl


database = Database()
# print(database.get_airport_by_distance("large_airport", 500))
fl.fly_menu(database, 500)
