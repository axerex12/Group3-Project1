from flightgame.db.Database import Database
from flightgame.contract.contracter import ContractClient

class GameClient:
    def __init__(self, db: Database):
        self.db = db
        self.id = 0 # save data didn't find this when creating a new session
        self.co2_consumed = 0
        self.co2_budget = 100
        self.currency = 100000
        self.rented_plane = None
        self.location= db.get_random_airport(1)[0]
        self.fuel_amount = 10000
        self.current_day = 0
        self.rent_amount = 0
        self.airport_type = None
        self.cargo = []
        self.gameover = False
        self.rent_paid = False
        self.screen_name = ""
        # Initialize the ContractClient
        self.contract_client = ContractClient(self.db)
        # Initialize current_contract to None
        self.current_contract = None

    def input_screen_name(self) -> str:
        while True:
            try:
                screen_name = input("Give your nickname: ")
                return screen_name
            except ValueError as e:
                print(e)
                return ""
            
    def new_session(self):
        """
        creates an user and adds it to the database
        """
        try:
            name = self.input_screen_name()
            if self.db.user_exists_by_name(name):
                return
            self.screen_name = name
        except Exception as e:
            print(e)
            return
        self.db.add_data([{"co2_consumed": self.co2_consumed, "co2_budget": self.co2_budget,
                            "currency": self.currency, "location": self.location["ident"],
                            "fuel_amount": self.fuel_amount, "current_day": self.current_day,
                            "screen_name": self.screen_name,
                          }], "game")
        #Generoi pelaajan ensinmäisen contractin
        self.current_contract = self.contract_client.contract_generator(self.screen_name)

    def load_session(self):
        data = self.db.fetch_data_row("game", "screen_name", '=', f'"{self.input_screen_name()}"')
        self.id = data['id']
        self.co2_consumed = data['co2_consumed']
        self.co2_budget = data['co2_budget']
        self.screen_name = data['screen_name']
        location = data["location"]
        self.location = self.db.fetch_data_row("airport", "ident", "=", f'"{location}"')
        self.currency = data['currency']
        rented_plane = data["rented_plane"]
        self.rented_plane = self.db.fetch_data_row("plane", "id", "=", f'"{rented_plane}"')
        self.fuel_amount = data['fuel_amount']
        self.current_day = data['current_day']
        self.rent_amount = int(self.rented_plane["fuel_consumption"]) + int(self.rented_plane["max_speed"]) * 50
        # set the airport type to be searched by the type of the plane
        if (self.rented_plane["type"] == "helicopter"):
            self.airport_type = "heliport"
        else:
            self.airport_type = "large_airport"

    def print_game_data(self):
        string = f"""_________________________________________
        \nLocation = {self.location["ident"]} - {self.location["name"]}
        \nFuel amount = {self.fuel_amount}
        \nCurrent day = {self.current_day}
        \nCurrency = {self.currency}
        _________________________________________
        """
        print(string)

    def save_game_data(self, user) -> bool:
        data = self.db.fetch_data_row("game", "screen_name", '=', f'"{user}"')
        if data is not None:
            # print(data)
            data['co2_consumed'] = self.co2_consumed
            data['co2_budget'] = self.co2_budget
            data['screen_name'] = user  # varmistaa että tallentaa samalla nimellä millä haettiin
            data['location'] = self.location["ident"]
            data['currency'] = self.currency
            data['rented_plane'] = self.rented_plane["id"]
            data['fuel_amount'] = self.fuel_amount
            data['current_day'] = self.current_day
            outputdata = [data]
            # print(outputdata)
            self.db.update_data(outputdata, "game", "screen_name")
            return True
        else: return False

    def check_contract_delivery(self):
        """tarkistaa jos pelaaja on contractin päämäärässä."""
        if self.current_contract:
            if self.location == self.current_contract['destination_id']:
                print("You have arrived at the destination airport!")
                # Pay the player and generate a new contract
                reward = self.current_contract['palkkio']
                self.db.update_currency_amount(reward, "+", self.screen_name)
                print(f"You have delivered the cargo! You earned {reward}€.")
                # Generate a new contract
                self.current_contract = self.contract_client.contract_generator(self.screen_name)
            else:
                print("This is not the destination for your contract.")