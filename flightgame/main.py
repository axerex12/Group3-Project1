from flightgame.db.Database import Database

db = Database()
#print(db.get_airport("EFHK"))
#print(db.get_current_schema())
#print(db.generate_alter_statements())
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
    },
    {
        "id": 3,
        "delivery_value": 50000,
        "weight": 500,
        "description": "biohazardous material"
    },
    {
        "id": 4,
        "delivery_value": 75000,
        "weight": 800,
        "description": "radioactive waste"
    },
    {
        "id": 5,
        "delivery_value": 250000,
        "weight": 1500,
        "description": "stolen art masterpiece"
    },
    {
        "id": 6,
        "delivery_value": 30000,
        "weight": 300,
        "description": "high-grade military equipment"
    },
    {
        "id": 7,
        "delivery_value": 10000,
        "weight": 100,
        "description": "chemical warfare agent"
    },
    {
        "id": 8,
        "delivery_value": 500000,
        "weight": 2500,
        "description": "classified government documents"
    },
    {
        "id": 9,
        "delivery_value": 120000,
        "weight": 1200,
        "description": "illegally trafficked rare animal"
    },
    {
        "id": 10,
        "delivery_value": 300000,
        "weight": 1700,
        "description": "antique treasure chest"
    },
    {
        "id": 11,
        "delivery_value": 45000,
        "weight": 350,
        "description": "unstable isotope"
    },
    {
        "id": 12,
        "delivery_value": 70000,
        "weight": 750,
        "description": "prohibited synthetic drug"
    },
    {
        "id": 13,
        "delivery_value": 1000000,
        "weight": 5000,
        "description": "extremely rare gemstone"
    },
    {
        "id": 14,
        "delivery_value": 90000,
        "weight": 800,
        "description": "smuggled weaponry"
    },
    {
        "id": 15,
        "delivery_value": 450000,
        "weight": 2200,
        "description": "counterfeit currency plates"
    },
    {
        "id": 16,
        "delivery_value": 15000,
        "weight": 250,
        "description": "highly toxic chemicals"
    },
    {
        "id": 17,
        "delivery_value": 400000,
        "weight": 2700,
        "description": "ancient scrolls"
    },
    {
        "id": 18,
        "delivery_value": 85000,
        "weight": 950,
        "description": "stolen luxury vehicle"
    },
    {
        "id": 19,
        "delivery_value": 200000,
        "weight": 1800,
        "description": "unauthorized biological sample"
    },
    {
        "id": 20,
        "delivery_value": 60000,
        "weight": 400,
        "description": "encrypted intelligence files"
    },
    {
        "id": 21,
        "delivery_value": 750000,
        "weight": 3200,
        "description": "prototype AI technology"
    },
    {
        "id": 22,
        "delivery_value": 100000,
        "weight": 1100,
        "description": "confiscated cartel assets"
    },
    {
        "id": 23,
        "delivery_value": 50000,
        "weight": 650,
        "description": "smuggled antiquities"
    },
    {
        "id": 24,
        "delivery_value": 25000,
        "weight": 350,
        "description": "illegal mining equipment"
    },
    {
        "id": 25,
        "delivery_value": 900000,
        "weight": 4500,
        "description": "experimental space tech component"
    }
]

plane_test = [
    {
        "id": 1,
        "type": "helicopter",
        "fuel_consumption": 200,
        "max_speed": 200
    },
    {
        "id": 2,
        "type": "cargo_plane",
        "fuel_consumption": 400,
        "max_speed": 800
    },
    {
        "id": 3,
        "type": "small_plane",
        "fuel_consumption": 150,
        "max_speed": 350
    },
    {
        "id": 4,
        "type": "helicopter",
        "fuel_consumption": 180,
        "max_speed": 220
    },
    {
        "id": 5,
        "type": "cargo_plane",
        "fuel_consumption": 500,
        "max_speed": 900
    },
    {
        "id": 6,
        "type": "small_plane",
        "fuel_consumption": 140,
        "max_speed": 330
    },
    {
        "id": 7,
        "type": "helicopter",
        "fuel_consumption": 220,
        "max_speed": 210
    },
    {
        "id": 8,
        "type": "cargo_plane",
        "fuel_consumption": 450,
        "max_speed": 820
    },
    {
        "id": 9,
        "type": "small_plane",
        "fuel_consumption": 160,
        "max_speed": 340
    },
    {
        "id": 10,
        "type": "helicopter",
        "fuel_consumption": 190,
        "max_speed": 180
    },
    {
        "id": 11,
        "type": "cargo_plane",
        "fuel_consumption": 550,
        "max_speed": 850
    },
    {
        "id": 12,
        "type": "small_plane",
        "fuel_consumption": 130,
        "max_speed": 360
    },
    {
        "id": 13,
        "type": "helicopter",
        "fuel_consumption": 240,
        "max_speed": 230
    },
    {
        "id": 14,
        "type": "cargo_plane",
        "fuel_consumption": 480,
        "max_speed": 780
    },
    {
        "id": 15,
        "type": "small_plane",
        "fuel_consumption": 155,
        "max_speed": 320
    },
    {
        "id": 16,
        "type": "helicopter",
        "fuel_consumption": 205,
        "max_speed": 195
    },
    {
        "id": 17,
        "type": "cargo_plane",
        "fuel_consumption": 520,
        "max_speed": 830
    },
    {
        "id": 18,
        "type": "small_plane",
        "fuel_consumption": 170,
        "max_speed": 340
    },
    {
        "id": 19,
        "type": "helicopter",
        "fuel_consumption": 185,
        "max_speed": 210
    },
    {
        "id": 20,
        "type": "cargo_plane",
        "fuel_consumption": 430,
        "max_speed": 810
    },
    {
        "id": 21,
        "type": "small_plane",
        "fuel_consumption": 145,
        "max_speed": 370
    },
    {
        "id": 22,
        "type": "helicopter",
        "fuel_consumption": 225,
        "max_speed": 240
    },
    {
        "id": 23,
        "type": "cargo_plane",
        "fuel_consumption": 600,
        "max_speed": 890
    },
    {
        "id": 24,
        "type": "small_plane",
        "fuel_consumption": 160,
        "max_speed": 355
    },
    {
        "id": 25,
        "type": "helicopter",
        "fuel_consumption": 250,
        "max_speed": 250
    }
]
#db.add_data(list(cargo_test),"cargo")
#db.add_data(list(plane_test), "plane")
print("Hi")
