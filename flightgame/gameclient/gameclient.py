from mysql.connector.errors import ErrorClassTypes

from flightgame.db.Database import Database

class GameClient:
    def __init__(self, db: Database):
        self.db = db
        self.co2_consumed = 0
        self.co2_budget = 100
        self.currency = 100000
        self.rented_plane = 1
        self.location= db.get_random_airport(1)[0]
        self.fuel_amount = 10000
        self.current_day = 0
        self.cargo = []
        
        try:
            self.screen_name = input("Give your nickname: ")
        except Exception as e:
            print(e)
            return

        self.db.add_data([{"co2_consumed": self.co2_consumed, "co2_budget": self.co2_budget,
                            "currency": self.currency, "location": self.location["ident"],
                            "fuel_amount": self.fuel_amount, "current_day": self.current_day,
                            "screen_name": self.screen_name, "rented_plane": self.rented_plane,
                          }], "game")
        

    def new_session(self, user, location):
        self.screen_name = user
        self.location = location

    def load_session(self, user):
        data = self.db.fetch_data_row("game", "screen_name", '=', f'"{user}"')[0]
        self.id = data['id']
        self.co2_consumed = data['co2_consumed']
        self.co2_budget = data['co2_budget']
        self.screen_name = data['screen_name']
        self.location = data['location']
        self.currency = data['currency']
        self.rented_plane = data['rented_plane']
        self.fuel_amount = data['fuel_amount']
        self.current_day = data['current_day']

    def print_game_data(self):
        string = f"""_________________________________________
        \nLocation = {self.location["ident"]} - {self.location["name"]}
        \nFuel amount = {self.fuel_amount}
        \nCurrent day = {self.current_day}
        \nCurrency = {self.currency}
        _________________________________________
        """
        print(string)

    def save_game_data(self, user):
        newsave = False
        data = self.db.fetch_data_row("game", "screen_name", '=', f'"{user}"')[0]
        print(data)
        if data['id'] is None:
            data['id'] = int(self.db.fetch_data_max("game","id")[0]['Output'])+1
            newsave = True
        else:
            data['id'] = self.id
        data['co2_consumed'] = self.co2_consumed
        data['co2_budget'] = self.co2_budget
        data['screen_name'] = user #varmistaa että tallentaa samalla nimellä millä haettiin
        data['location'] = self.location
        data['currency'] = self.currency
        data['rented_plane'] = self.rented_plane
        data['fuel_amount'] = self.fuel_amount
        data['current_day'] = self.current_day
        outputdata = [data]
        print(outputdata)
        if newsave:
            self.db.add_data(outputdata,"game")
        else:
            self.db.update_data(outputdata,"game","id")