import pygame.mouse


class Plane:
    x=0
    y=0

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
        if(self.x < 1920):
            for i in range (5):
                misile = Missile()



