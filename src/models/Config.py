import os
import sys
from abc import ABC

from pygame import *
from pygame.display import *

from src.resources import Device


class Config(ABC):
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
        self.device = Device()
        self.screen = display.set_mode(self.device.get_display(), RESIZABLE)
        self.refresh_rate = self.device.get_refresh_rate()

        # set the icon and the caption of the game
        set_icon(self.icon)
        set_caption("Sprout Lands")

    def update(self):
        print(self.device.get_display())

        for e in event.get():
            self.event_type = e.type

            if e.type == KEYUP:
                self.event_key = e.key

            if self.event_type == QUIT:
                self.exit()

            if self.event_key == K_ESCAPE:
                self.start = False
                sys.exit()

        # update the delta time and clock tick rate
        # to keep the game running at the same speed
        # on all devices
        self.delta_time = self.clock.tick(self.FPS) / 1000.0

        display.update()

    def load_music(self, filename: str):
        mixer.init()
        music = mixer.music

        music.load(
            f"{os.path.join(os.getcwd(), 'assets', 'music')}/{filename}")
        music.play()

    @property
    def icon(self):
        return image.load(f"{os.path.join(os.getcwd(), 'assets', 'icons')}/icon.png")

    @property
    def diff(self):
        return self.game_speed * self.delta_time
