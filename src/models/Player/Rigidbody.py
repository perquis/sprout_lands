import os
from abc import ABC
from typing import List

from pygame import *
from pygame.sprite import Sprite

from src.enums import Direction


class Rigidbody(ABC, Sprite):
    def __init__(self, speed: float) -> None:
        Sprite.__init__(self)

        x, y = display.get_window_size()

        # return the path to the spritesheet
        keywords = ["Basic", "Charakter", "Spritesheet"]
        dirname = " ".join(keywords)
        filename = "_".join(keywords)
        CHARACTER_PATH = 'assets/packages/sprites_basic_pack/Characters'

        self.__filename = f"{CHARACTER_PATH}/{dirname}/{filename}"

        # return default properties of the player
        self.__current_direction = Direction.DOWN
        self.__player_pos = Vector2(x / 2, y / 2)
        self.__current_sprite = 0.0
        self.__speed = speed

        # return the state of the player
        # based on the action he is performing
        self.__is_move = False
        self.__is_chop_tree = False
        self.__is_plow_field = False
        self.__is_water_plants = False

        # return a list of images by direction
        # (up, down, left, right) based on idleness
        self.__sprites_idle_up = self.load_sprites(
            self.__filename, Direction.UP)
        self.__sprites_idle_down = self.load_sprites(
            self.__filename, Direction.DOWN)
        self.__sprites_idle_left = self.load_sprites(
            self.__filename, Direction.LEFT)
        self.__sprites_idle_right = self.load_sprites(
            self.__filename, Direction.RIGHT)

        # return a list of images by direction
        # (up, down, left, right) based on movement
        self.__sprites_move_up = self.load_sprites(
            self.__filename, Direction.UP, range(3, 5))
        self.__sprites_move_down = self.load_sprites(
            self.__filename, Direction.DOWN, range(3, 5))
        self.__sprites_move_left = self.load_sprites(
            self.__filename, Direction.LEFT, range(3, 5))
        self.__sprites_move_right = self.load_sprites(
            self.__filename, Direction.RIGHT, range(3, 5))

        # return a list of keys that are responsible
        # for the movement of the player
        self.__direction_up_keys: List[bool] = []
        self.__direction_down_keys: List[bool] = []
        self.__direction_left_keys: List[bool] = []
        self.__direction_right_keys: List[bool] = []
        self.__all_direction_keys: List[bool] = []

        # get the rectangle object that has the dimensions
        self.image = self.__sprites_idle_down[int(self.__current_sprite)]
        # return the rectangle object of the image
        self.rect = self.image.get_rect()

    def toggle_move(self, is_move: bool) -> None:
        self.__is_move = is_move

    def toggle_water_platns(self, is_water_plants: bool) -> None:
        self.__is_water_plants = is_water_plants

    def toggle_chop_tree(self, is_chop_tree: bool) -> None:
        self.__is_chop_tree = is_chop_tree

    def toggle_plow_field(self, is_plow_field: bool) -> None:
        self.__is_plow_field = is_plow_field

    def load_sprites(self, filename: str, direction: Direction, range=range(1, 3)):
        return [
            image.load(f"{filename}_{direction}_{index}.png")
            for index in range
        ]

    def set_current_image(self, movement, idleness) -> None:
        self.image = movement if self.__is_move else idleness

    def update(self, diff: float) -> None:
        self.get_pressed_keys()
        self.animation()

        self.movement(diff)
        self.water_plants()
        self.plow_field()
        self.chop_tree()

    def animation(self) -> None:
        self.rect.center = self.__player_pos
        self.__current_sprite += self.__speed * 0.1

        # reset the animation if the current sprite
        # is greater than the length of the list
        if self.__current_sprite >= len(self.__sprites_idle_down):
            self.__current_sprite = 0.0

        # handle the player animation based on
        # the direction and movement or idleness
        n = int(self.__current_sprite)

        match self.__current_direction:
            case Direction.UP:
                self.set_current_image(
                    self.__sprites_move_up[n],
                    self.__sprites_idle_up[n]
                )
            case Direction.DOWN:
                self.set_current_image(
                    self.__sprites_move_down[n],
                    self.__sprites_idle_down[n]
                )
            case Direction.LEFT:
                self.set_current_image(
                    self.__sprites_move_left[n],
                    self.__sprites_idle_left[n]
                )
            case Direction.RIGHT:
                self.set_current_image(
                    self.__sprites_move_right[n],
                    self.__sprites_idle_right[n]
                )

    def water_plants(self) -> None:
        keys = key.get_pressed()

        if keys[K_SPACE]:
            self.toggle_water_platns(True)
        else:
            self.toggle_water_platns(False)

    def chop_tree(self) -> None:
        keys = key.get_pressed()

        if keys[K_SPACE]:
            self.toggle_chop_tree(True)
        else:
            self.toggle_chop_tree(False)

    def plow_field(self) -> None:
        keys = key.get_pressed()

        if keys[K_SPACE]:
            self.toggle_plow_field(True)
        else:
            self.toggle_plow_field(False)

    def movement(self, diff: float) -> None:
        # handle the player idle animation
        if any(self.__direction_up_keys):
            self.__current_direction = Direction.UP
            self.__player_pos.y -= diff
        if any(self.__direction_down_keys):
            self.__current_direction = Direction.DOWN
            self.__player_pos.y += diff
        if any(self.__direction_left_keys):
            self.__current_direction = Direction.LEFT
            self.__player_pos.x -= diff
        if any(self.__direction_right_keys):
            self.__current_direction = Direction.RIGHT
            self.__player_pos.x += diff

        # handle the player movement animation
        if any(self.__all_direction_keys):
            self.toggle_move(True)
        else:
            self.toggle_move(False)

    def get_pressed_keys(self):
        keys = key.get_pressed()

        self.__direction_up_keys = [
            keys[K_w],
            keys[K_UP]
        ]
        self.__direction_down_keys = [
            keys[K_s],
            keys[K_DOWN]
        ]
        self.__direction_left_keys = [
            keys[K_a],
            keys[K_LEFT]
        ]
        self.__direction_right_keys = [
            keys[K_d],
            keys[K_RIGHT]
        ]
        self.__all_direction_keys = [
            *self.__direction_up_keys,
            *self.__direction_down_keys,
            *self.__direction_left_keys,
            *self.__direction_right_keys
        ]
