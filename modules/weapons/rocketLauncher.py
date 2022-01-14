from modules.players.player import Player
import time


class Rocket_Launcher:

    x = 0
    y = 0

    def __init__(self, player):
        self.x = player.x
        self.y = player.y


    def before_fall(self):
        a = 3
        for i in range (3):
            time.sleep(1)
        return True

    def traj(self, gravity, wind, window):
        #trajectoire = polynôme du second degré
        courbe =


if __name__ == '__main__':
    player = Player(50, 0)
    rlaunch = Rocket_Launcher(player)
    print(rlaunch.x)

    player.x = 150
    rlaunch2 = Rocket_Launcher(player)
    print(rlaunch2.x)
    rlaunch.before_explosion()