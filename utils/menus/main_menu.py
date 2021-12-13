from utils.buttons.NewGameButton import NewGameButton
from utils.config.config import Config
from utils.info.info import Info
from utils.info.info import State


class MainMenu:

    BTN_NEW_GAME = NewGameButton()


    @staticmethod
    def switch():
        MainMenu.draw()
        Info.state = State.MAIN_MENU

    @staticmethod
    def draw():
        Config.window.blit(Config.IMG_BACKGROUND, (0, 0))
        MainMenu.BTN_NEW_GAME.draw()