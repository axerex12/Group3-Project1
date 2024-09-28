from flightgame.db.Database import Database
import flightgame.flying.flying as fl


database = Database()
print(database.get_airport_by_distance("large_airport", 500))
