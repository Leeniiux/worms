import numpy

from config import Config


class Trajectory:
    projectile = None
    origin = None
    speed = None
    wind = None
    points = []
    iterator = 0

    def calculate(self):
        coords = self.origin
        while coords[0] <= Config.WINDOW_W and coords[1] <= Config.WINDOW_H:
            coords[0] = coords[0] + self.speed[0]
            coords[1] = coords[1] + self.speed[1]
            self.speed[0] = self.speed[0] - (6*self.projectile.radius*numpy.pi/self.projectile.mass) - (self.wind/self.projectile.mass)
            self.speed[1] = self.speed[1] + (6*self.projectile.radius*numpy.pi/self.projectile.mass) + (self.wind/self.projectile.mass) + (Config.GRAVITY/self.projectile.mass)
            self.points.append(coords)

    def __init__(self, projectile, origin, speed, wind):
        self.projectile = projectile
        self.origin = origin
        self.speed = speed
        self.wind = wind
        self.calculate()

    def next(self):
        self.iterator = self.iterator + 1
        return self.coords[self.iterator]