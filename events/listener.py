from utils.info.info import Info
from utils.info.info import State


class Listener:

    @staticmethod
    def startingListener():
        return

    @staticmethod
    def event():
        if Info.state == State.STARTING:
            Listener.startingListener()
