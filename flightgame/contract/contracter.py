import random
import mysql.connector

'''
Generoi kontracti että minne pitää mennä ja mikä cargo ja paljonko siitä saa
'''
#valitsee random lentökentän id
def contract_generator():
    cursor.execute("SELECT * FROM airport ORDER BY RAND() LIMIT 1")
    random_airport = cursor.fetchone()
    airport_id = random_airport[0]
    #random lentokentän nimi
    dest_ap_name = random_airport[3]
#ottaa random cargon id arvon painon ja kuvauksen ylös
    cursor.execute("SELECT * FROM cargo ORDER BY RAND() LIMIT 1")
    random_cargo = cursor.fetchone()
    cargo_id = random_cargo[0]
    cargo_value = random_cargo[1]
    cargo_weight = random_cargo[2]
    cargo_description = random_cargo[3]
# random raha määrä contractille!
    random_money_value = random.randint(1000, 1000000)

    contract = {
        "destination_id": airport_id,  # lentokentän ident
        "cargo_id": cargo_id,  # cargo id
        "cargo_value": cargo_value,  # cargon arvo
        "cargo_weight": cargo_weight,  # Cargo paino
        "cargo_description": cargo_description, #cargo kuvaus
    }
    print(contract)
    print(f"sinun pitää viedä paketti {dest_ap_name} lentokenttään")
    print(f"Cargossa on: {contract["cargo_description"]} ja se on arvoltaan{contract["cargo_value"]} paino on {contract["cargo_weight"]}")
    print(f"Palkkio paketin viemisestä ajallaan on: {random_money_value}")
