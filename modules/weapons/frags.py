from modules.players.player import Player

from modules.weapons.frag_rocket import Frag_Rocket
class Frags:
    x=0
    y=0

    def __init__(self):
        self.x = Frag_Rocket.get_coor_before_frag()[0]
        self.y = Frag_Rocket.get_coor_before_frag()[1]

