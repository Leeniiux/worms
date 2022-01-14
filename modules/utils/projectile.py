from config import Config
from modules.utils.trajectory import Trajectory


class Projectile:

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
        self.x = 0
        self.y = 0

    def getTrajectory(self, pos, speed):
        return Trajectory(self, pos, speed, Config.WIND)