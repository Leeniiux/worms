from player import *
from game_config import *
class GameState :
    def __init__(self):
        self.player = Player(20)

    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))