import random
import numpy

import config
from map.map import Map


class MapBuilder:

    @staticmethod
    def generate(type): # True for island, False for inside
        # Générer plusieurs formes, de tailles définies et à des endroits définis. Les formes, elles, sont aléatoires
        res = None
        if type:
            res = Map(MapBuilder.generateForm(config.Config.WINDOW_W - config.Config.WINDOW_W / 10, config.Config.WINDOW_H / 1.3, 10, 100, config.Config.WINDOW_W / 2, config.Config.WINDOW_H))
        else :
            pass
        pass
        return res

    @staticmethod
    def generateForm(width, height, range, points, posx, posy):
        increment = 2*numpy.pi/points
        a = width/2
        b = height/2
        form = []
        t = 0
        while t < 2*numpy.pi:
            x = a*numpy.cos(t) + random.gauss(0, range)
            y = b*numpy.sin(t) + random.gauss(0, range)
            form.append((x+posx, y+posy))
            t += increment
        return numpy.array(form)