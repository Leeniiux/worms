import random

import numpy
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
            p = Config.TEAM.current()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if math.fabs(p.y - Config.MAP.getY(p.x)) <= 5:
                    p.speedY = Config.FORCE_JUMP
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                p.speedLeft = -5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                p.speedRight = 5
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                p.speedLeft = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                p.speedRight = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                p.switchWeapon()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = [p.x, p.y - 30]
                mouse = pygame.mouse.get_pos()
                speed = [(mouse[0] - pos[0]), (mouse[1] - pos[1])]
                p.getWeapon().throw(pos, speed)
    return False


def display(window):
    if Config.STATE == "starting":
        # Action de démarrage
        Config.STATE = "main_menu"
        return

    if Config.STATE == "main_menu":
        window.blit(Files.IMG_BACKGROUND_BOTH, (0, 0))
        #window.blit(Files.IMG_NEW_GAME, ((Config.WINDOW_W-Files.IMG_NEW_GAME_W)/2, (Config.WINDOW_H-Files.IMG_NEW_GAME_H)/2))
        render = Config.FONT.render("Press SPACE to start the game !", False, (0, 0, 0))
        window.blit(render, (Config.WINDOW_W/2-render.get_width()/2, Config.WINDOW_H/2-render.get_height()/2))
        return

    if Config.STATE == "init":
        Config.STATE = "game"

        # Generating map
        Config.MAP = MapBuilder.generate(True)
        Config.WIND = random.randint(-5, 5)

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
        # Displaying players and thrown weapons
        for p in Config.TEAM.players:
            p.move()
            pygame.draw.ellipse(window, Config.TEAM.color, pygame.Rect(p.x-10, p.y-50, 20, 60), 0)
            render = Config.FONT.render(str(p.health), False, (0, 0, 0))
            window.blit(render, (p.x-render.get_width()/2, p.y - 120))
            for w in p.weapons:
                if w.throwing:
                    next = w.trajectory.next()
                    if next:
                        ymap = Config.MAP.getY(next[0])
                        if next[1] >= ymap:
                            w.throwing = False
                            w.explode(next)
                        else:
                            pygame.draw.circle(window, pygame.color.Color(20, 20, 20), next, 8, 0)

        #Draw trajectory
        current = Config.TEAM.current()
        weapon = current.getWeapon()
        pos = [current.x, current.y-30]
        mouse = pygame.mouse.get_pos()
        speed = [(mouse[0] - pos[0]), (mouse[1] - pos[1])]

        points = weapon.getTrajectory(pos, speed).points
        pygame.draw.aalines(window, pygame.color.Color(255, 255, 255), False, points, 8)
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
        pygame.time.delay(30)


def main():
    # Initialisations
    pygame.init()
    pygame.font.init()
    Config.FONT = pygame.font.SysFont('Comic Sans MS', 30)
    Files.init()
    window = pygame.display.set_mode((Config.WINDOW_W, Config.WINDOW_H))

    # Boucle de jeu
    loop(window)

    # Arrêt du système
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
