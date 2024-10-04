from flightgame.db.Database import Database

class GameClient:
    def __init__(self, db: Database):
        self.co2_consumed = 0
        self.co2_budget = 100
        self.screen_name = "temp"
        self.location= "temp"
        self.currency = 100000
        self.rented_plane = 1
        self.fuel_amount = 100
        self.current_day = 0
        self.cargo = []
        self.db = db

    def load_session(self, user):
        data = self.db.fetch_data_row("game", "screen_name", '=', user)
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
        string = f"""_________________________________________
        \nLocation = {self.location} - {self.db.get_airport(self.location)}
        \nFuel amount = {self.fuel_amount}
        \nCurrent day = {self.current_day}
        \nCurrency = {self.currency}
        _________________________________________
        """
        print(string)
