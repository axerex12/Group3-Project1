import random
from flightgame.db.Database import Database

db = Database()

'''
Generoi kontracti että minne pitää mennä ja mikä cargo ja paljonko siitä saa
'''
#valitsee random lentökentän id
def contract_generator():
    contracts = []
    for i in range(3):
        # random raha määrä contractille!
        random_money_value = random.randint(1000, 1000000)
        airport = db.get_random_airport(1)[0]
        cargo = db.get_random_cargo(1)[0]


        contract = {
            "destination_id": airport["ident"],  # lentokentän ident
            "cargo_id": cargo["id"],  # cargo id
            "cargo_value": cargo["delivery_value"],  # cargon arvo
            "cargo_weight": cargo["weight"],  # Cargo paino
            "cargo_description": cargo["description"], #cargo kuvaus
            "palkkio":random_money_value,
            "name":airport["name"]
        }
        contracts.append(contract)
    for idx, contract in enumerate(contracts, start=1):
        print(f"\nKontrakti {idx}:")
        print(f"Lentokenttä: {contract['name']}")
        print(f"Cargo ID: {contract['cargo_id']}")
        print(f"Cargon kuvaus: {contract['cargo_description']}")
        print(f"Cargon arvo: {contract['cargo_value']}")
        print(f"Cargon paino: {contract['cargo_weight']}")
        print(f"Palkkio: {contract['palkkio']}")
    while True:
        choice = int(input("\nValitse kontrakti (1-3): ")) - 1
        if 0 <= choice < 3:
            selected_contract = contracts[choice]
            print(f"\nValittu kontrakti:")
            #print(selected_contract)
            print(f"Lentokenttä: {selected_contract['name']}")
            print(f"Cargo ID: {selected_contract['cargo_id']}")
            print(f"Cargon kuvaus: {selected_contract['cargo_description']}")
            print(f"Cargon arvo: {selected_contract['cargo_value']}")
            print(f"Cargon paino: {selected_contract['cargo_weight']}")
            print(f"Palkkio: {selected_contract['palkkio']}")
            return selected_contract
        else:
            print("Virheellinen valinta. Valitse 1, 2 tai 3.")
contract_generator()