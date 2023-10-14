from abc import ABC
from typing import List

import pygame as pg

from packages.enums import Direction
from packages.utils.images import find_images_by_direction as fibd


class Rigidbody(ABC, pg.sprite.Sprite):
    """
    Rigidbody is a class that is responsible for
    the movement of the player.
    """

    def __init__(self, pos_x, pos_y, speed) -> None:
        pg.sprite.Sprite.__init__(self)

        self.current_direction = Direction.DOWN
        self.player_pos = pg.Vector2(pos_x, pos_y)
        self.current_sprite = 0.0
        self.is_move = False
        self.speed = speed

        # return a list of images by direction (up, down, left, right) based on idleness
        self.__sprites_idle_up = fibd(Direction.UP)
        self.__sprites_idle_down = fibd(Direction.DOWN)
        self.__sprites_idle_left = fibd(Direction.LEFT)
        self.__sprites_idle_right = fibd(Direction.RIGHT)

        # return a list of images by direction (up, down, left, right) based on movement
        self.__sprites_move_up = fibd(Direction.UP, range(3, 5))
        self.__sprites_move_down = fibd(Direction.DOWN, range(3, 5))
        self.__sprites_move_left = fibd(Direction.LEFT, range(3, 5))
        self.__sprites_move_right = fibd(Direction.RIGHT, range(3, 5))

        # return a list of keys that are responsible for the movement of the player
        self.__direction_up_keys: List[bool] = []
        self.__direction_down_keys: List[bool] = []
        self.__direction_left_keys: List[bool] = []
        self.__direction_right_keys: List[bool] = []
        self.__all_direction_keys: List[bool] = []

        # get the rectangle object that has the dimensions
        self.image = self.__sprites_idle_down[int(self.current_sprite)]
        # return the rectangle object of the image
        self.rect = self.image.get_rect()

    def update(self, diff: float) -> None:
        self.animation()
        self.movement(diff)

    def animation(self):
        """Handles the animation of the player based on the current sprite."""
        self.rect.center = self.player_pos
        self.current_sprite += self.speed * 0.1

        # reset the animation if the current sprite is greater than the length of the list
        if self.current_sprite >= len(self.__sprites_idle_down):
            self.current_sprite = 0.0

        # handle the player animation based on the direction and movement or idleness
        if self.current_direction == Direction.UP and not self.is_move:
            self.image = self.__sprites_idle_up[int(self.current_sprite)]
        elif self.current_direction == Direction.DOWN and not self.is_move:
            self.image = self.__sprites_idle_down[int(self.current_sprite)]
        elif self.current_direction == Direction.LEFT and not self.is_move:
            self.image = self.__sprites_idle_left[int(self.current_sprite)]
        elif self.current_direction == Direction.RIGHT and not self.is_move:
            self.image = self.__sprites_idle_right[int(self.current_sprite)]
        elif self.current_direction == Direction.UP and self.is_move:
            self.image = self.__sprites_move_up[int(self.current_sprite)]
        elif self.current_direction == Direction.DOWN and self.is_move:
            self.image = self.__sprites_move_down[int(self.current_sprite)]
        elif self.current_direction == Direction.LEFT and self.is_move:
            self.image = self.__sprites_move_left[int(self.current_sprite)]
        elif self.current_direction == Direction.RIGHT and self.is_move:
            self.image = self.__sprites_move_right[int(self.current_sprite)]

    def movement(self, diff: float) -> None:
        """Handles the movement of the player."""
        keys = pg.key.get_pressed()

        self.__direction_up_keys = [
            keys[pg.K_w],
            keys[pg.K_UP]
        ]
        self.__direction_down_keys = [
            keys[pg.K_s],
            keys[pg.K_DOWN]
        ]
        self.__direction_left_keys = [
            keys[pg.K_a],
            keys[pg.K_LEFT]
        ]
        self.__direction_right_keys = [
            keys[pg.K_d],
            keys[pg.K_RIGHT]
        ]
        self.__all_direction_keys = [
            *self.__direction_up_keys,
            *self.__direction_down_keys,
            *self.__direction_left_keys,
            *self.__direction_right_keys
        ]

        # handle the player idle animation
        if any(self.__direction_up_keys):
            self.current_direction = Direction.UP
            self.player_pos.y -= diff
        if any(self.__direction_down_keys):
            self.current_direction = Direction.DOWN
            self.player_pos.y += diff
        if any(self.__direction_left_keys):
            self.current_direction = Direction.LEFT
            self.player_pos.x -= diff
        if any(self.__direction_right_keys):
            self.current_direction = Direction.RIGHT
            self.player_pos.x += diff

        # handle the player movement animation
        if any(self.__all_direction_keys):
            self.toggle_move(True)
        else:
            self.toggle_move(False)

    def toggle_move(self, is_move: bool) -> None:
        self.is_move = is_move
