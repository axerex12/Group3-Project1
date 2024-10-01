import random
import mysql.connector
import flightgame.db.Database
from flightgame.db.Database import Database

db = Database()

'''
Generoi kontracti että minne pitää mennä ja mikä cargo ja paljonko siitä saa
'''
#valitsee random lentökentän id
def contract_generator():
    airport = db.get_random_airport(1)[0]
#ottaa random cargon id arvon painon ja kuvauksen ylös
    cargo = db.get_random_cargo(1)[0]
# random raha määrä contractille!
    random_money_value = random.randint(1000, 1000000)

    contract = {
        "destination_id": airport["ident"],  # lentokentän ident
        "cargo_id": cargo["id"],  # cargo id
        "cargo_value": cargo["delivery_value"],  # cargon arvo
        "cargo_weight": cargo["weight"],  # Cargo paino
        "cargo_description": cargo["description"], #cargo kuvaus
    }
    print(contract)
    print(f"sinun pitää viedä paketti {airport['name']} lentokenttään")
    print(f"Cargossa on: {contract['cargo_description']} ja se on arvoltaan {contract['cargo_value']} paino on {contract['cargo_weight']}")
    print(f"Palkkio paketin viemisestä ajallaan on: {random_money_value}")

contract_generator()