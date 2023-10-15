from abc import ABC

import pygame

from packages import models, resources


class API(ABC):
    """The API for the game."""

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

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
        self.screen = pygame.display.set_mode(self.display, pygame.RESIZABLE)
        self.refresh_rate = device.get_refresh_rate()

    @property
    def is_fullscreen(self) -> bool:
        """
        Return True if the game is in 
        fullscreen mode, False otherwise.
        """
        return pygame.display.is_fullscreen()

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
        for event in pygame.event.get():
            self.event_type = event.type

            if event.type == pygame.KEYUP:
                self.event_key = event.key

        # update the delta time and clock tick rate
        # to keep the game running at the same speed
        # on all devices
        self.delta_time = self.clock.tick(self.refresh_rate) / 1000

        pygame.display.update()

    def handle_events(self):
        """
        Handle the events:

        - exit the game if the user clicks the close button
        - toggle fullscreen mode if the user presses the F11 key
        - exit the game if the user presses the ESC key
        """
        if self.event_type == pygame.QUIT:
            self.exit()

        if self.event_type == pygame.KEYUP and self.event_key == pygame.K_F11:
            self.mouse_visible(self.is_fullscreen)
            self.toggle_fullscreen()

        if self.event_key == pygame.K_ESCAPE:
            self.exit()

    def mouse_visible(self, visible: bool):
        """Show or hide the mouse."""
        pygame.mouse.set_visible(visible)

    def load_music(self, music: str):
        """Load the music."""
        resources.music(music)

    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        pygame.display.toggle_fullscreen()

    def exit(self):
        """Exit the game."""
        self.start = False
