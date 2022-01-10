from game_config import *
from tests.AvoidBats.game_state import GameState


def game_loop(window):
    quitting = False
    game_state = GameState()
    while not quitting:
        game_state.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True


def main():
    pygame.init()
    GameConfig.init()
    window = pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
    pygame.display.set_caption("Avoid Bats")
    game_loop(window)
    pygame.quit()
    quit()


main()
