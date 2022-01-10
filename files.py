import pygame


class Files:
    IMG_BACKGROUND_BOTH = None

    IMG_NEW_GAME = None
    IMG_NEW_GAME_W = 600
    IMG_NEW_GAME_H = 250

    @staticmethod
    def init():
        Files.IMG_BACKGROUND_BOTH = pygame.image.load("assets/images/background/both.png")

        Files.IMG_NEW_GAME = pygame.image.load("assets/images/buttons/new_game.png")

