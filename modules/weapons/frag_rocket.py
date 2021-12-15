from modules.players.player import Player
import time


class Frag_Rocket:

    x = 0
    y = 0

    def __init__(self, player):
        self.x = player.x
        self.y = player.y

    def get_coor_before_frag(self):
        return self.x, self.y

    def before_frag(self):
        a = 3
        for i in range (3):
            print(a)
            time.sleep(1)
            a-=1
        return True
