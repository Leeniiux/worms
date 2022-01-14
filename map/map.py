import random

import numpy as np

from config import Config


class Map:
    points = []

    def __init__(self, points):
        self.points = points

    def getY(self, x):
        res = None
        last = self.points[len(self.points)-1]
        for p in self.points:
            if last[0] < x < p[0] or last[0] > x > p[0]:
                a = (last[1]-p[1])/(last[0]-p[0])
                b = last[1]-a*last[0]
                y = a*x+b
                if res is None or y < res:
                    res = y
            last = p
        return res

    def spreadPlayers(self, team):
        a = np.linspace(Config.WINDOW_W/5, Config.WINDOW_W-Config.WINDOW_W/5, 20)
        # Spread every player around the map (entirely randomly)
        for p in team.players:
            # Random X that matches limited height
            x = a[random.randint(0, 19)]
            while self.getY(x) > Config.WINDOW_H:
                x = a[random.randint(0, 19)]
            p.x = x
            p.y = self.getY(x)-100
