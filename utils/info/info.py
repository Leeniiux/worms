from utils.info.states import State
from utils.menus.main_menu import MainMenu


class Info:

    state = None


    def __init__(self):
        self.state = State.STARTING


    def next(self):
        if self.state == State.STARTING:
            MainMenu.switch()
