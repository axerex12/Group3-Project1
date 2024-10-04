from flightgame.db.Database import Database

class GameClient:
    def __init__(self, database: Database):
        self.co2_consumed = 0
        self.co2_budget = 100
        self.screen_name = "vesa"
        self.location= "temp"
        self.currency = 100000
        self.rented_plane = 1
        self.fuel_amount = 100
        self.current_day = 0
        self.cargo = []
        self.db = database

    def load_session(self,db: Database, user):
        data = db.get_data_row(("game", user), "game")
        self.co2_consumed = data['co2_consumed']
        self.co2_budget = data['co2_budget']
        self.screen_name = data['screen_name']
        self.location = data['location']
        self.currency = data['currency']
        self.rented_plane = data['rented_plane']
        self.fuel_amount = data['fuel_amount']
        self.current_day = data['current_day']
        self.cargo = data['cargo']

    def print_game_data(self):
        game_state = self.db.get_data_row(("screen_name", self.screen_name), "game")
        string = f"""_________________________________________
\nLocation = {game_state["location"]} - {self.db.get_airport(game_state["location"])["name"]}
Fuel amount = {game_state["fuel_amount"]}
Current day = {game_state["current_day"]}
Currency = {game_state["currency"]}
_________________________________________
        """
        print(string)
