import pygame

from modules.players.player import Player


class Team:

    players = []
    color = pygame.color.Color(209, 106, 42)
    iterator = 0

    def __init__(self):
        for i in range(5):
            self.players.append(Player(0, 0))

    def current(self):
        if len(self.players) <= 0:
            return None
        elif len(self.players) <= self.iterator:
            self.iterator = 0
        return self.players[self.iterator]

    def next(self):
        self.iterator += 1
        return self.current()