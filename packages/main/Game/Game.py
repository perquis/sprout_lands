import os

import pygame as pg

from packages.main.Game.API import API
from packages.models.Player.Player import Player


class Game(API):
    """🎮 The game. 🎮"""

    def __init__(self) -> None:
        super().__init__()
        self.player = Player("PerQuis", speed=0.5)

    def run(self):
        """Run the game."""
        # toggle the fullscreen when the game is in production mode
        if os.getenv("MODE") == "production":
            self.toggle_fullscreen()

        # load default settings of the game
        self.mouse_visible(False)
        self.load_music("village_vibe.mp3")

        # create the player group and add the player to it
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
