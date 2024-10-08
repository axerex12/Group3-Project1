from flightgame.gameclient.gameclient import GameClient
from flightgame.flying.flying import Flying
from flightgame.rentaplane.Planerenting import Planerenting
import story
#Temporary, proof of concept

def main_menu(game_client: GameClient):
    fl = Flying(game_client)
    pr = Planerenting(game_client)

    gameName = "Boeing Simulator 2024"
    search_radius = 600

    print("""
    //////////////////////////////////////////////////////////////
    //__        __   _                            _             //
    //\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___       //
    // \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \      //
    //  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |     //
    // __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   _  //
    //|  _ \| | __ _ _ __   ___    __ _  __ _ _ __ ___   ___| | //
    //| |_) | |/ _` | '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \ | //
    //|  __/| | (_| | | | |  __/ | (_| | (_| | | | | | |  __/_| //
    //|_|   |_|\__,_|_| |_|\___|  \__, |\__,_|_| |_| |_|\___(_) //
    //                            |___/                         //
    //////////////////////////////////////////////////////////////
    """)

    #TODO: check player rented plane and change fly_meny to search for correct type
    while True:
        game_client.gameover = False
        print(f"## {gameName} ##\n1) New Session\n2) Load previous session\n3) Credits\n4) Exit\n5) Story")
        userInput = input("> ")
        if userInput == "1":
            game_client.new_session()
            pr.renting_menu()
            fl.fly_menu(game_client.airport_type, search_radius)
        elif userInput == "2":
            game_client.load_session()
            fl.fly_menu(game_client.airport_type, search_radius)
        elif userInput == "3":
            print()
            continue
        elif userInput == "4":
            exit(0)
        elif userInput == "5":
            for line in story.getStory():
                print(line)
        else:
            print("Invalid input, retry.")