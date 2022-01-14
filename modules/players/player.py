import pygame

from config import Config
from modules.weapons.grenade import Grenade


class Player:
    x = 0
    y = 0
    speedLeft = 0
    speedRight = 0
    speedY = 0

    health = 100

    mass = 10

    current_weapon = 0
    weapons = [Grenade()]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_position_mine(self):
        if(pygame.mouse.get_pressed(1)):
            x=pygame.mouse.get_pos()[0]
            y=pygame.mouse.get_pos()[1]
        return x,y

    def get_position(self):
        return self.x, self.y

    def move(self):
        self.x += self.speedLeft + self.speedRight

        self.y += self.speedY
        self.speedY += Config.GRAVITY/self.mass

        temp = Config.MAP.getY(self.x)
        if self.y >= temp:
            self.y = temp
            self.speedY = 0


    def switchWeapon(self):
        self.current_weapon += 1
        if len(self.weapons) <= self.current_weapon:
            self.current_weapon = 0

    def getWeapon(self):
        return self.weapons[self.current_weapon]