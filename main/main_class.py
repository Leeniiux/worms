import pygame

from utils.config.config import Config
from utils.files.files import Files
from utils.info.info import Info
from modules.players.player import Player

class Main:

    FILES = None
    CONFIG = None
    INFO = None
    PLAYER = None
    @staticmethod
    def init():
        pygame.init()
        Main.FILES = Files()
        Main.CONFIG = Config()
        Main.INFO = Info()
        Main.PLAYER = Player()