import random
import numpy

import config
from map.map import Map


class MapBuilder:

    @staticmethod
    def generate(type): # True for outside, False for inside
        # Générer plusieurs formes, de tailles définies et à des endroits définis. Les formes, elles, sont aléatoires
        map = Map()
        if type:
            map.addForm(MapBuilder.generateForm(config.Config.WINDOW_H/3, config.Config.WINDOW_H/3, 10, 100) + 100)
            map.addForm(MapBuilder.generateForm(config.Config.WINDOW_H, config.Config.WINDOW_H/3, 10, 100) + 350)
            map.addForm(MapBuilder.generateForm(config.Config.WINDOW_H/3, config.Config.WINDOW_H/3, 10, 100) + 600)
        else :
            pass
        pass
        return map

    @staticmethod # MapBuilder.generateForm(500, 100, 20, 10) + 500
    def generateForm(width, height, range, points):
        increment = 2*numpy.pi/points
        a = width/2
        b = height/2
        form = []
        t = 0
        while t < 2*numpy.pi:
            x = a*numpy.cos(t) + random.gauss(0, range)
            y = b*numpy.sin(t) + random.gauss(0, range)
            form.append((x, y))
            t += increment
        return numpy.array(form)