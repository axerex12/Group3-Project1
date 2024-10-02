from flightgame.db.Database import Database
from geopy import distance

db = Database()


def calculate_distance(icao1: str, icao2: str) -> float:
    """
    Laskee etäisyyden lentokenttien välillä ICAO-koodin avulla
    käyttäen lentokenttien longitude ja latitude käyttäen geopy.distance.

    :param icao1: Ensimmäisen lentokentän ICAO-koodi.
    :param icao2: Toisen lentokentän ICAO-koodi.
    :return: Etäisyys kilometreinä.
    """
    airport1 = db.get_airport(icao1)
    airport2 = db.get_airport(icao2)

    if airport1 is None or airport2 is None:
        raise ValueError("Yhtä tai molempia lentokenttiä ei löytynyt.")

    ap1_cords = (airport1['latitude_deg'], airport1['longitude_deg'])
    ap2_cords = (airport2['latitude_deg'], airport2['longitude_deg'])

    dist = distance.distance(ap1_cords, ap2_cords).kilometers
    return dist


def print_contract(contract):
    """Tulostaa sopimuksen tiedot."""
    print(f"Lentokenttä: {contract['airport_name']}")
    print(f"Cargon kuvaus: {contract['cargo_description']}")
    print(f"Cargon arvo: {contract['cargo_value']}€")
    print(f"Cargon paino: {contract['cargo_weight']}kg")
    print(f"Palkkio: {contract['palkkio']}€")
    print(f"Etäisyys nykyisestä lentokentästä: {contract['distance']:.2f} km")


def contract_generator() -> dict:
    """Generoi 3 satunnaista kontraktia, joista pelaaja voi valita yhden."""
    contracts = []
    current_airport = db.get_current_airport("heini")

    for _ in range(3):
        airport = db.get_random_airport(1)[0]
        cargo = db.get_random_cargo(1)[0]
        palkkio = 0.2 * cargo['delivery_value']  # Palkkio on 20% cargon arvosta
        distance_to_airport = calculate_distance(current_airport['ident'], airport['ident'])

        contract = {
            "destination_id": airport["ident"],
            "cargo_id": cargo["id"],
            "cargo_value": cargo["delivery_value"],
            "cargo_weight": cargo["weight"],
            "cargo_description": cargo["description"],
            "palkkio": palkkio,
            "airport_name": airport["name"],
            "distance": distance_to_airport
        }
        contracts.append(contract)

    # Tulostetaan sopimukset
    for idx, contract in enumerate(contracts, start=1):
        print(f"\nKontrakti {idx}:")
        print_contract(contract)

    selected_contract = select_contract(contracts)
    print("\nValittu kontrakti:")
    print_contract(selected_contract)
    return selected_contract


def select_contract(contracts) -> dict:
    """Pelaaja valitsee kontraktin 1-3."""
    while True:
        try:
            choice = int(input("\nValitse kontrakti (1-3): ")) - 1
            if 0 <= choice < len(contracts):
                return contracts[choice]
            else:
                print("Virheellinen valinta. Valitse numero 1, 2 tai 3.")
        except ValueError:
            print("Syötä numero 1-3.")


# Kutsutaan kontraktigeneraattoria
contract_generator()