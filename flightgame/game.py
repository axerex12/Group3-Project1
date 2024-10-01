import story
from flightgame.db.Database import Database
db = Database()

storyDialog = input('Do you want to read the background story? (Y/N): ')
if storyDialog == 'Y':
    # print wrapped string line by line
    for line in story.getStory():
        print(line)


print('When you are ready to start, ')
player = input('type player name: ')
# boolean for game over and win
game_over = False
score = 0

start_airport = db.get_random_airport(1)[0]







