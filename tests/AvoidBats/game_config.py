import pygame


class GameConfig:
    windowH = 640
    windowW = 960
    Y_PLATEFORM = 516
    PLAYER_W = 64
    PLAYER_H = 64

    def init():
        GameConfig.BACKGROUND_IMG = pygame.image.load('ressources/background.png')
