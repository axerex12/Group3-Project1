from flightgame.db.Database import Database

class GameClient:
    def __init__(self):
        co2_consumed = 0
        co2_budget = 100
        screen_name = "temp"
        location= "temp"
        currency = 100000
        rented_plane = 1
        fuel_amount = 100
        current_day = 0
        cargo = []

    def load_session(self,db: Database, user):
        data = db.fetch_data_row("game","user","=",f'{user}')[0]
        co2_consumed = data['co2_consumed']
        co2_budget = data['co2_budget']
        screen_name = data['screen_name']
        location = data['location']
        currency = data['currency']
        rented_plane = data['rented_plane']
        fuel_amount = data['fuel_amount']
        current_day = data['current_day']
        cargo = data['cargo']