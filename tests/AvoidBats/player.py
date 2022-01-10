import pygame
from game_config import *
class Player(pygame.sprite.Sprite) :
    def __init__(self,x):
        self.rect = pygame.Rect(x,
                                GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H,
                                GameConfig.PLAYER_W,
                                GameConfig.PLAYER_H)

