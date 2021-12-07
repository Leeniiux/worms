import pygame

from events.listener import Listener
from utils.game_config import Config
from utils.game_info import Info


def loop():
    while Config.running:
        Listener.event()
        Info.next()
        pygame.display.update()


def main():
    pygame.init()
    Config.init()
    Config.window = pygame.display.set_mode((Config.WINDOW_W, Config.WINDOW_H))
    pygame.display.set_caption("Worms Game !")
    loop()


if __name__ == '__main__':
    main()
