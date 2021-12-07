import pygame.image

from utils.game_config import Config
from utils.game_info import Info
from utils.states import State


class MainMenu:

    IMG_BACKGROUND = pygame.image.load('assets/menus/main_menu/background.png')
    IMG_BACKGROUND_W = Config.WINDOW_W
    IMG_BACKGROUND_H = Config.WINDOW_H
    
    IMG_NEW_GAME = pygame.image.load('assets/main_menu/img_new_game.png')
    IMG_NEW_GAME_W = Config.WINDOW_W/2
    IMG_NEW_GAME_H = Config.WINDOW_H/6

    @staticmethod
    def switch():
        MainMenu.draw()
        Info.state = State.MAIN_MENU

    @staticmethod
    def draw():
        Config.window.blit(MainMenu.IMG_BACKGROUND, (0, 0))
        Config.window.blit(MainMenu.IMG_NEW_GAME, (Config.WINDOW_W/2-MainMenu.IMG_NEW_GAME_W/2, Config.WINDOW_H/2-MainMenu.IMG_NEW_GAME_H/2))