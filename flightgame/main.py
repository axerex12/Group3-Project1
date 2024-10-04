from flightgame.db.Database import Database
from flightgame.flying.encounters import EncounterClient
from flightgame.gameclient.gameclient import GameClient
from flightgame.data import Data # here is all of the cargo = [] etc. to declutter main.py
import mainMenu

enc = EncounterClient()
db = Database()
gc = GameClient(db)

mainMenu.main_menu(gc)