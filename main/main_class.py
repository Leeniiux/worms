import pygame

from utils.config.config import Config
from utils.files.files import Files
from utils.info.info import Info


class Main:

    FILES = None
    CONFIG = None
    INFO = None

    @staticmethod
    def init():
        pygame.init()
        Main.FILES = Files()
        Main.CONFIG = Config()
        Main.INFO = Info()
