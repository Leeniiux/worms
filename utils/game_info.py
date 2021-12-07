from utils.menus.main_menu import MainMenu
from utils.states import State


class Info:

    state = State.STARTING

    @staticmethod
    def next():
        if Info.state == State.STARTING:
            MainMenu.switch()
