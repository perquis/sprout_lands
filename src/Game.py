from pygame import *

from .models import Config, Player


class Game(Config):
    def __init__(self) -> None:
        super().__init__()
        self.player = Player("PerQuis", speed=0.5)

    def run(self):
        mouse.set_visible(False)
        display.toggle_fullscreen()

        # load default settings of the game
        self.load_music()

        # create the player group and add the player to it
        players_group = sprite.Group()
        players_group.add(self.player)

        while self.start:
            # update the sprites and draw them to the screen
            # based on the Player model and his properties
            # (speed, direction, etc.)
            players_group.update(self.diff)
            players_group.draw(self.screen)

            # update the game and handle the events
            # after drawing the sprites to the screen
            # based on the API model
            self.update()

            # fill the screen with black color to avoid
            # the effect of "traces" of the player
            # on the screen after movement (animation)
            self.screen.fill("cyan")
