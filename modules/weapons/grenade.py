import pygame.mouse
import math

import main
from modules.players.player import Player
import time


class Grenade:

    x = 0
    y = 0
    MASSE = 5
    r = 0.1
    def __init__(self, player):
        self.x = player.x
        self.y = player.y


    def before_explosion(self):
        a = 3
        for i in range (3):
            print(a)
            time.sleep(1)
            a-=1
        print("boom")









if __name__ == '__main__':
    player = Player(50, 0)
    grenade = Grenade(player)
    print(grenade.x)

    player.x = 150
    grenade2 = Grenade(player)
    print(grenade2.x)
    grenade.before_explosion()