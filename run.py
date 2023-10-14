import pygame as pg

from packages.main import Game
from packages.models import Player

if __name__ == '__main__':
    pg.init()

    # create the player and the game
    player = Player("PerQuis", speed=0.25)
    game = Game(player)

    # run the game
    game.run()

    pg.quit()
