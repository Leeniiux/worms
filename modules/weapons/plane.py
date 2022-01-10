import time

import pygame.mouse

from modules.weapons.missile import Missile


class Plane:
    x=-20
    y=-20

    def __init__(self):
        self.x = 0
        self.y = 1000

    def get_coor(self):
        return self.x, self.y

    def fly(self):
        while(self.x <1950):
            self.x += 20

    def move_forward(self, x):
        self.x += 20

    def throw_bombs(self):
        ev=pygame.event.get()
        currentPosX=self.x
        currentPosY=self.y
        if(self.x < 1920 and pygame.mouse.get_pressed(1)):
            for i in range (5):
                misile = Missile(currentPosX, currentPosY)
                time.sleep(1)


