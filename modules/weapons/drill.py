from modules.players.player import Player
import time

class Drill:

    x = 0
    y = 0

    def __init__(self, player):
        self.x = player.x
        self.y = player.y


    def before_explosion(self):
        a = 5
        for i in range (5):
            print(a)
            time.sleep(1)
            a-=1
        print("boom")

if __name__ == '__main__':
    player = Player(50, 0)
    drill = Drill(player)
    print(drill.x)

    player.x = 150
    drill2 = Drill(player)
    print(drill2.x)
    drill.before_explosion()