import pygame

from events.listener import Listener
from main_class import Main
from utils.config.config import Config


def loop():
    while Config.running:
        Listener.event()
        Main.INFO.next()
        pygame.display.update()


def main():
    Main.init()
    Config.window = pygame.display.set_mode((Config.WINDOW_W, Config.WINDOW_H))
    pygame.display.set_caption("Worms Game !")
    loop()


if __name__ == '__main__':
    main()
