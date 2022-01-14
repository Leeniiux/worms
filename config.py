import pygame


class Config:
    FONT = None
    WIND = 0
    MAP = None
    TEAM = None

    WINDOW_W = 1200
    WINDOW_H = 720

    IMG_NEW_GAME_W = 600
    IMG_NEW_GAME_H = 250

    STATE = "starting"

    GRAVITY = 9.81
    FORCE_JUMP = -9.81
    @staticmethod
    def init():
        Config.IMG_BACKGROUND_BOTH = pygame.image.load("assets/images/background/background.jpg")
        Config.IMG_BACKGROUND_BOTH = pygame.transform(Config.IMG_BACKGROUND_BOTH, (Config.WINDOW_W, Config.WINDOW_H))
        Config.IMG_NEW_GAME = pygame.image.load("assets/images/buttons/new_game.png")

