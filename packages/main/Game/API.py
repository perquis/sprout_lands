from abc import ABC

import pygame as pg

from packages import models, resources


class API(ABC):
    """The API for the game."""

    def __init__(self) -> None:
        self.clock = pg.time.Clock()

        # initialize core properties of the game
        self.start = True
        self.event_type = None
        self.event_key = None
        self.delta_time = 0.0
        self.game_speed = 225

        # set the display and the refresh rate
        # of the game
        device = models.Device()
        self.display = device.get_display()
        self.screen = pg.display.set_mode(self.display, pg.RESIZABLE)
        self.refresh_rate = device.get_refresh_rate()

        # set the icon and the caption of the game
        pg.display.set_icon(self.icon)
        pg.display.set_caption("Sprout Lands")

    @property
    def icon(self):
        """Return the icon of the game."""
        return resources.character(
            "Basic Charakter Spritesheet/Basic_Charakter_Spritesheet_DOWN_1.png"
        )

    @property
    def is_fullscreen(self) -> bool:
        """
        Return True if the game is in 
        fullscreen mode, False otherwise.
        """
        return pg.display.is_fullscreen()

    @property
    def diff(self):
        """Return the speed multiplied by the delta time."""
        return self.game_speed * self.delta_time

    def update(self):
        """
        Update the game:

        - get the events
        - update the delta time and clock tick rate
        - update the display
        """
        for event in pg.event.get():
            self.event_type = event.type

            if event.type == pg.KEYUP:
                self.event_key = event.key

        # update the delta time and clock tick rate
        # to keep the game running at the same speed
        # on all devices

        # implement calculation for delta time
        # to reduce the speed of the game for
        # the players with a slow computer
        self.delta_time = self.clock.tick(self.refresh_rate) / 1000

        pg.display.update()

    def handle_events(self):
        """
        Handle the events:

        - exit the game if the user clicks the close button
        - toggle fullscreen mode if the user presses the F11 key
        - exit the game if the user presses the ESC key
        """
        if self.event_type == pg.QUIT:
            self.exit()

        if self.event_type == pg.KEYUP and self.event_key == pg.K_F11:
            self.mouse_visible(self.is_fullscreen)
            self.toggle_fullscreen()

        if self.event_key == pg.K_ESCAPE:
            self.exit()

    def mouse_visible(self, visible: bool):
        """Show or hide the mouse."""
        pg.mouse.set_visible(visible)

    def load_music(self, music: str):
        """Load the music."""
        resources.music(music)

    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        pg.display.toggle_fullscreen()

    def exit(self):
        """Exit the game."""
        self.start = False
