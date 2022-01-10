import pygame

from config import Config
from files import Files
from map.map_builder import MapBuilder


def listen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

        # Main menu
        if Config.STATE == "main_menu":
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Config.STATE = "init"

    return False


def display(window):
    if Config.STATE == "starting":
        # Action de démarrage
        Config.STATE = "main_menu"
        return

    if Config.STATE == "main_menu":
        window.blit(Files.IMG_BACKGROUND_BOTH, (0, 0))
        window.blit(Files.IMG_NEW_GAME, (0, 0))
        return

    if Config.STATE == "init":
        Config.STATE = "game"
        Config.MAP = MapBuilder.generate(True)
        display(window)
        return

    if Config.STATE == "game":
        window.blit(Files.IMG_BACKGROUND_BOTH, (0, 0))
        for p in Config.MAP.forms:
            pygame.draw.polygon(window, points=p, color=pygame.color.Color(227, 71, 245), width=5)
        return


def loop(window):
    quitting = False

    # Game Loop
    while not quitting:
        # Event Listener
        quitting = listen()
        # Affichage
        display(window)
        pygame.display.update()



def main():
    # Initialisations
    pygame.init()
    Files.init()
    window = pygame.display.set_mode((Config.WINDOW_W, Config.WINDOW_H))

    # Boucle de jeu
    loop(window)

    # Arrêt du système
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
