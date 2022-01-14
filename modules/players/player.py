import pygame


class Player:
    x = 0
    y = 0

    speedX = 0
    speedY = 0

    health = 100

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