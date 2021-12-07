from modules.players.player import Player


class Grenade:

    x = 0
    y = 0

    def __init__(self, player):
        self.x = player.x
        self.y = player.y


if __name__ == '__main__':
    player = Player(50, 0)
    grenade = Grenade(player)
    print(grenade.x)

    player.x = 150
    grenade2 = Grenade(player)
    print(grenade2.x)
