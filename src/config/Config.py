import sys
from abc import ABC

from pygame import *

from src.resources import Device
from src.router import Router

router = Router()


class Config(ABC):
    """The Config for the game."""

    def __init__(self) -> None:
        self.clock = time.Clock()

        # initialize core properties of the game
        self.start = True
        self.event_type = None
        self.event_key = None
        self.delta_time = 0.0
        self.game_speed = 225.0
        self.FPS = 60.0

        # set the display and the refresh rate
        # of the game
        device = Device()
        self.screen = display.set_mode((1280, 720), RESIZABLE)
        self.refresh_rate = device.get_refresh_rate()

        # set the icon and the caption of the game
        display.set_icon(self.icon)
        display.set_caption("Sprout Lands")

    @property
    def icon(self):
        """Return the icon of the game."""
        return image.load(
            f"{router.sprites}/Basic Charakter Spritesheet/Basic_Charakter_Spritesheet_DOWN_1.png"
        )

    @property
    def is_fullscreen(self) -> bool:
        """
        Return True if the game is in 
        fullscreen mode, False otherwise.
        """
        return display.is_fullscreen()

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
        for e in event.get():
            self.event_type = e.type

            if e.type == KEYUP:
                self.event_key = e.key

        # update the delta time and clock tick rate
        # to keep the game running at the same speed
        # on all devices
        self.delta_time = self.clock.tick(self.FPS) / 1000.0

        display.update()

    def handle_events(self):
        """
        Handle the events:

        - exit the game if the user clicks the close button
        - toggle fullscreen mode if the user presses the F11 key
        - exit the game if the user presses the ESC key
        """
        if self.event_type == QUIT:
            self.exit()

        if self.event_type == KEYUP and self.event_key == K_F11:
            self.mouse_visible(self.is_fullscreen)
            self.toggle_fullscreen()

        if self.event_key == K_ESCAPE:
            self.exit()
            sys.exit()

    def mouse_visible(self, visible: bool):
        """Show or hide the mouse."""
        mouse.set_visible(visible)

    def load_music(self, filename: str):
        """Load the music."""
        mixer.init()
        music = mixer.music

        music.load(f"{router.music}/{filename}")
        music.play()

    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        display.toggle_fullscreen()

    def exit(self):
        """Exit the game."""
        self.start = False
        sys.exit()
