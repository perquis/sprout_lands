import pygame as pg

from packages.main.Game.API import API
from packages.models import Player


class Game(API):
    """🎮 The game. 🎮"""

    def __init__(self, player: Player) -> None:
        super().__init__()
        self.player = player

    def run(self):
        """Run the game."""
        self.toggle_fullscreen()
        self.mouse_visible(False)
        self.load_music("village_vibe.mp3")

        players_group = pg.sprite.Group()
        players_group.add(self.player)

        while self.start:
            # update the sprites and draw them to the screen
            # based on the Player model and his properties
            # (speed, direction, etc.)
            players_group.update(diff=self.diff)
            players_group.draw(surface=self.screen)

            # update the game and handle the events
            # after drawing the sprites to the screen
            # based on the API model
            self.update()
            self.handle_events()

            # fill the screen with black color to avoid
            # the effect of "traces" of the player
            # on the screen after movement (animation)
            self.screen.fill("black")
