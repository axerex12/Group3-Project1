#Temporary, proof of concept
gameName = "Boeing Simulator 2024"
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
print(f"## {gameName} ##\n1) New Session\n2) Load previous session\n3) Credits\n4) Exit")

while True:
    userInput = input()
    if userInput == "1":
        # no code yet
        print()
        break
    elif userInput == "2":
        print()
    elif userInput == "3":
        print()
    elif userInput == "4":
        exit(1)
    else:
        print("Invalid input, retry.")
print("test")