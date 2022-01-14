import math

from config import Config
from modules.utils import projectile


class Grenade(projectile.Projectile):

    uses = 0
    max_uses = 2
    range = 50
    max_damage = 80

    throwing = False
    trajectory = None

    def __init__(self):
        super().__init__(5, 1)


    def throw(self, pos, speed):
        if self.uses >= self.max_uses:
            return False
        # self.uses += 1

        self.trajectory = self.getTrajectory(pos, speed)
        self.throwing = True

    def explode(self, pos):
        for p in Config.TEAM.players:
            dist = math.sqrt(math.pow(p.x-pos[0], 2) + math.pow(p.y-pos[1], 2))
            if dist <= self.range:
                dmg = int(self.max_damage - self.max_damage*dist/self.range)
                p.health -= dmg
                if p.health <= 0:
                    Config.TEAM.players.remove(p)
