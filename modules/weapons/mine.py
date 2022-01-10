from modules.players.player import Player
import time


class Mine:

    x = 0
    y = 0

    def __init__(self):
        self.x = player.set_position_mine()[0]
        self.y = player.set_position_mine()[1]


    def explosion(self, playerx, playery):
        explosion = False
        if(playerx == self.x and playery == self.y):
            print("boom")
            explosion = True
        return explosion

if __name__ == '__main__':
    player = Player(50, 0)
    mine = Mine()
    print(mine.x)

    player.x = 150
    mine2 = Mine()
    print(mine2.x)
    mine.explosion()