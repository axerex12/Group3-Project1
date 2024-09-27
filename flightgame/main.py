from flightgame.db.Database import Database

db = Database()
print(db.get_airport("EFHK"))
print(db.get_current_schema())
print(db.generate_alter_statements())
#print(db.get_current_schema())

cargo_test = [
	{
		"id": 1,
		"delivery_value": 20000,
		"weight": 200,
		"description": "dangerous and highly explosive"
	},
	{
		"id": 2,
		"delivery_value": 150000,
		"weight": 2000,
		"description": "highly illegal"
	}
]
plane_test = [
	{
		"id":1,
		"type":"helicopter",
		"fuel_consumption": 200,
		"max_speed": 200,
	},
	{
		"id":2,
		"type":"cargo_plane",
		"fuel_consumption": 400,
		"max_speed": 800,
	}
]
db.add_data(list(plane_test),"plane")

