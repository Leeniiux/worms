import pygame

from utils.config.config import Config


class Files:

    IMG_BACKGROUND_BOTH = None
    IMG_BACKGROUND_BOTH_W = Config.WINDOW_W
    IMG_BACKGROUND_BOTH_H = Config.WINDOW_H

    IMG_NEW_GAME = None
    IMG_NEW_GAME_W = Config.WINDOW_W / 2
    IMG_NEW_GAME_H = Config.WINDOW_H / 6

    BTN_NEW_GAME = None


    def __init__(self):
        self.IMG_BACKGROUND_BOTH = pygame.image.load('assets/menus/main_menu/background.png')
        self.IMG_NEW_GAME = pygame.image.load('assets/menus/main_menu/img_new_game.png')