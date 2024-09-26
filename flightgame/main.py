from flightgame.db.Database import Database

db = Database()
print(db.get_airport("EFHK"))
db.validate_database()
print(db.get_current_schema())