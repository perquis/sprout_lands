from abc import ABC
from typing import List

import pygame

from packages import models, resources


class Settings(ABC):
    """🔧 The game settings. 🔧"""

    def __init__(self) -> None:
        pygame.init()

        device = models.Device()
        resolution = pygame.display.Info()

        self.start = True
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

        self.event_type = None
        self.event_key = None

        self.display = resolution.current_w, resolution.current_h
        self.screen = pygame.display.set_mode(self.display, pygame.RESIZABLE)
        self.refresh_rate = device.get_refresh_rate()

        self.delta_time = 0.0
        self.speed = 225

        self.direction_up_keys: List[bool] = []
        self.direction_down_keys: List[bool] = []
        self.direction_left_keys: List[bool] = []
        self.direction_right_keys: List[bool] = []
        self.all_direction_keys: List[bool] = []

    def update(self):
        """Update the game."""
        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            self.event_type = event.type

            if event.type == pygame.KEYUP:
                self.event_key = event.key

        # update the direction keys to keep the player moving in the same direction
        self.direction_up_keys = [
            self.keys[pygame.K_w], self.keys[pygame.K_UP]]
        self.direction_down_keys = [
            self.keys[pygame.K_s], self.keys[pygame.K_DOWN]]
        self.direction_left_keys = [
            self.keys[pygame.K_a], self.keys[pygame.K_LEFT]]
        self.direction_right_keys = [
            self.keys[pygame.K_d], self.keys[pygame.K_RIGHT]]
        self.all_direction_keys = [*self.direction_up_keys, *self.direction_down_keys,
                                   *self.direction_left_keys, *self.direction_right_keys]

        pygame.display.update()
        # update the delta time and clock tick rate to keep the game running at the same speed on all devices
        self.delta_time = self.clock.tick(self.refresh_rate) / 1000

    def handle_events(self):
        """Handle the events."""
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
        resources.music("village_vibe.mp3")

    @property
    def is_fullscreen(self) -> bool:
        return pygame.display.is_fullscreen()

    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        pygame.display.toggle_fullscreen()

    def exit(self):
        """Exit the game."""
        self.start = False
