import pygame
import math
from config import Config
from files import Files
from map.map_builder import MapBuilder
from modules.players.team import Team


def listen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

        # Main menu
        if Config.STATE == "main_menu":
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Config.STATE = "init"

        # In game
        if Config.STATE == "game":
            Config.ACTION = []
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Config.ACTION.append("jump")
            if pygame.key.get_pressed()[pygame.K_q]:
                Config.ACTION.append("move_left")
            if pygame.key.get_pressed()[pygame.K_d]:
                Config.ACTION.append("move_right")

    return False


def display(window):
    if Config.STATE == "starting":
        # Action de démarrage
        Config.STATE = "main_menu"
        return

    if Config.STATE == "main_menu":
        window.blit(Files.IMG_BACKGROUND_BOTH, (0, 0))
        window.blit(Files.IMG_NEW_GAME, ((Config.WINDOW_W-Files.IMG_NEW_GAME_W)/2, (Config.WINDOW_H-Files.IMG_NEW_GAME_H)/2))
        #pygame.draw.polygon(window, points=MapBuilder.generateForm(500, 100, 20, 10) + 500, width=4, color=pygame.color.Color(20, 20, 20))
        return

    if Config.STATE == "init":
        Config.STATE = "game"

        # Generating map
        Config.MAP = MapBuilder.generate(True)

        # Generating teams
        Config.TEAM = Team()

        # Setting each player position
        Config.MAP.spreadPlayers(Config.TEAM)

        display(window)
        return

    if Config.STATE == "game":
        window.blit(Files.IMG_BACKGROUND_BOTH, (0, 0))

        # Displaying map
        pygame.draw.polygon(window, points=Config.MAP.points, color=pygame.color.Color(227, 71, 245), width=5)
        # Displaying players
        for p in Config.TEAM.players:
            pygame.draw.ellipse(window, Config.TEAM.color, pygame.Rect(p.x-10, p.y-50, 20, 60), 3)
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

def traj(self, window, weapon, wind, gravity):
    vectB = [self.x, self.y]
    vectA = None
    GRAVITY = 9,81
    if (pygame.mouse.get_pressed(1)):
        vectA = [pygame.mouse.get_pos()]
    pygame.draw.line(window, pygame.color.Color(20, 20, 20), vectA, vectB)
    speed = [vectB[0]-vectA[0], vectB[1]-vectA[1]]
    currentPos = vectB
    positions = []
    while not hitSurface() or not outOfBounds():
        positions.append(currentPos)
        oldpos = currentPos
        currentPos[0] = currentPos[0]+(-6*weapon.r*math.pi)/weapon.MASSE
        currentPos[1] = currentPos[1]+(6*weapon.r*math.pi+GRAVITY)/weapon.MASSE
        pygame.draw.arc(window, 000000, )




def outOfBounds():
    pass

def hitSurface():
    pass
if __name__ == '__main__':
    main()
