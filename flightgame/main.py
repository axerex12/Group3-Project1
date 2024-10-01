from flightgame.db.Database import Database
import flightgame.flying.flying as fl

db = Database()

planes = [
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

#db.add_data(planes,"plane")
while True:
    fl.fly_menu(db, distance=500, airport_type="large_airport", user="heini")
    # print(db.get_plane("heini"))
# db.update_values([{"type": "helicopter", "id": 1}], "plane", "id")
