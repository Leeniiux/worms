import pygame


class Map(pygame.sprite.Sprite):
    forms = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


    def addForm(self, points):
        self.forms.append(points)