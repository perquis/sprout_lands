import pygame as pg
from dotenv import load_dotenv

from src.Game import Game

if __name__ == '__main__':
    pg.init()
    load_dotenv()

    game = Game()
    game.run()

    pg.quit()
