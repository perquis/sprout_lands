from abc import ABC

import pygame as pg

from packages.enums import Direction
from packages.utils.images import find_images_by_direction as fibd


class Rigidbody(ABC, pg.sprite.Sprite):
    """
    Rigidbody is a class that is responsible for
    the movement of the player.
    """

    def __init__(self, pos_x, pos_y) -> None:
        pg.sprite.Sprite.__init__(self)

        self.player_pos = pg.Vector2(pos_x, pos_y)
        self.current_sprite = 0.0
        self.is_move = False

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

        # get the rectangle object that has the dimensions
        self.image = self.__sprites_idle_down[int(self.current_sprite)]
        # return the rectangle object of the image
        self.rect = self.image.get_rect()

    def update_player_pos(self, pos: pg.Vector2) -> None:
        self.player_pos = pos

    def toggle_move(self, is_move: bool) -> None:
        self.is_move = is_move

    def update(self, pos: pg.Vector2, speed: float, direction: Direction) -> None:
        self.rect.center = pos
        self.current_sprite += speed * 0.1

        if self.current_sprite >= len(self.__sprites_idle_down):
            self.current_sprite = 0.0

        if direction == Direction.UP and not self.is_move:
            self.image = self.__sprites_idle_up[int(self.current_sprite)]
        elif direction == Direction.DOWN and not self.is_move:
            self.image = self.__sprites_idle_down[int(self.current_sprite)]
        elif direction == Direction.LEFT and not self.is_move:
            self.image = self.__sprites_idle_left[int(self.current_sprite)]
        elif direction == Direction.RIGHT and not self.is_move:
            self.image = self.__sprites_idle_right[int(self.current_sprite)]
        elif direction == Direction.UP and self.is_move:
            self.image = self.__sprites_move_up[int(self.current_sprite)]
        elif direction == Direction.DOWN and self.is_move:
            self.image = self.__sprites_move_down[int(self.current_sprite)]
        elif direction == Direction.LEFT and self.is_move:
            self.image = self.__sprites_move_left[int(self.current_sprite)]
        elif direction == Direction.RIGHT and self.is_move:
            self.image = self.__sprites_move_right[int(self.current_sprite)]
