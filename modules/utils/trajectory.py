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
        while Config.WINDOW_H >= coords[1]:
            nx = coords[0] + self.speed[0]
            ny = coords[1] + self.speed[1]
            coords = [nx, ny]
            self.points.append(coords)
            self.speed[0] = self.speed[0] - 0.01*(1/250 * (6*self.projectile.radius*numpy.pi/self.projectile.mass*self.speed[0]) - self.wind/self.projectile.mass)
            self.speed[1] = self.speed[1] - 0.01*(-1 / 250 * (6 * self.projectile.radius * numpy.pi / self.projectile.mass * self.speed[1]) - Config.GRAVITY / self.projectile.mass)

    def __init__(self, projectile, origin, speed, wind):
        self.projectile = projectile
        self.origin = origin
        self.speed = speed
        self.speed[0] /= 20
        self.speed[1] /= 20
        self.wind = wind
        self.points = [origin]
        self.calculate()

    def next(self):
        self.iterator = self.iterator + 1
        if len(self.points) <= self.iterator:
            return False
        return self.points[self.iterator]