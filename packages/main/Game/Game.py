import pygame as pg

from packages.main.Game.API import API
from packages.models import Player


class Game(API):
    """🎮 The game. 🎮"""

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        """Run the game."""
        self.toggle_fullscreen()
        self.mouse_visible(False)
        self.load_music("village_vibe.mp3")

        new_player = Player("PerQuis", speed=0.25)

        sprites = pg.sprite.Group()
        sprites.add(new_player)

        while self.start:
            sprites.update(diff=self.diff)
            sprites.draw(surface=self.screen)

            self.update()
            self.handle_events()
            self.screen.fill("black")

        pg.quit()
