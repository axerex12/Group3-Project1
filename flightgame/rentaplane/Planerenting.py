from flightgame.db.Database import Database

db = Database()
#valitsee randomin lentokoneen
def plane_chooser():
    random_plane = db.get_random_plane(1)
    plane_price = (random_plane[2] + random_plane[3]) * 50
    random_plane[4] = plane_price
    return random_plane

def plane_format(random_plane, order_id):
    print(f"Vehicle type: {random_plane[1]}\nFuel consumption: {random_plane[2]}\nMax speed: {random_plane[3]}\nRenting Price: {random_plane[4]}\nID: {order_id}")

def renting_menu():
    i = 0
    j = 0
    max_planes = 3
    planes = []
    while i < max_planes:
        planes[i] = plane_chooser()
        plane_format(planes[i],i+1)
        i += 1
    while True:
        try:
            userInput = int(input("Which plane would you like to rent? "))
        except ValueError:
            print("Not an integer! Try again!")
            continue
        else:
            if (userInput <= 0) and (userInput > max_planes):
                print("Not a valid index! Try again!")
                continue
            else:
                print(planes[userInput-1])