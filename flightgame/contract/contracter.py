from flightgame.db.Database import Database
from geopy import distance

class ContractClient:

    def __init__(self, db: Database):
        self.database = db

    def calculate_distance(self,icao1: str, icao2: str) -> float:
        """laskee lentokenttien etäysyydet."""
        airport1 = self.database.get_airport(icao1)
        airport2 = self.database.get_airport(icao2)

        if airport1 is None or airport2 is None:
            raise ValueError("One or both airports could not be found.")

        ap1_cords = (airport1['latitude_deg'], airport1['longitude_deg'])
        ap2_cords = (airport2['latitude_deg'], airport2['longitude_deg'])

        dist = distance.distance(ap1_cords, ap2_cords).kilometers
        return dist

    def print_contract(self,contract: dict):
        """printtaa contractien tiedot."""
        print(f"Lentokenttä: {contract['airport_name']}")
        print(f"Cargon kuvaus: {contract['cargo_description']}")
        print(f"Cargon arvo: {contract['cargo_value']}€")
        print(f"Cargon paino: {contract['cargo_weight']}kg")
        print(f"Palkkio: {contract['palkkio']}€")
        print(f"Etäisyys nykyisestä lentokentästä: {contract['distance']:.2f} km")

    def contract_generator(self, user: str) -> dict:
        """Generoi 3 contractia pelaajalle ja antaa niistä infoa."""
        contracts = []
        current_airport = self.database.get_current_airport(user)

        if not current_airport:
            print("Error: Unable to retrieve current airport for the user.")
            return {}

        for _ in range(3):
            airport = self.database.get_random_airport(1)[0]
            cargo = self.database.get_random_cargo(1)[0]
            palkkio = 0.2 * cargo['delivery_value']  # Reward is 20% of cargo value
            distance_to_airport = self.calculate_distance(current_airport['ident'], airport['ident'])

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

        # Print contracts
        print("\nAvailable Contracts:")
        for idx, contract in enumerate(contracts, start=1):
            print(f"\nKontrakti {idx}:")
            self.print_contract(contract)

        selected_contract = self.select_contract(contracts)
        print("\nValittu kontrakti:")
        self.print_contract(selected_contract)
        return selected_contract

    def select_contract(self,contracts) -> dict:
        """Antaa pelaajan valita contracti 3 vaihto ehdosta"""
        while True:
            try:
                choice = int(input("\nValitse kontrakti (1-3): ")) - 1
                if 0 <= choice < len(contracts):
                    return contracts[choice]
                else:
                    print("Virheellinen valinta. Valitse numero 1, 2 tai 3.")
            except ValueError:
                print("Syötä numero 1-3.")

    def contract_destination(self,chosen_contract, user):
        """tarkistaa onko pelaaja saapunut kohde lento kenttään"""
        reward = chosen_contract['palkkio']
        current_airport = self.database.get_current_airport(user)

        if current_airport["ident"] == chosen_contract["destination_id"]:
            self.database.update_currency_amount(reward, "+", user)
            print(f"Sait vietyä paketin sovittuun määränpäähän! Tässä on sinun palkkiosi!: {reward}€")
            return self.contract_generator(user)  # Generate new contracts after successful delivery
        else:
            print("Et ole saapunut oikeaan lentokenttään. Yritä uudelleen.")
