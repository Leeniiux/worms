from utils.game_info import Info
from utils.states import State


class Listener:

    @staticmethod
    def startingListener():
        return

    @staticmethod
    def event():
        if Info.state == State.STARTING:
            Listener.startingListener()
