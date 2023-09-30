from abc import ABC
from packages.enums import Direction
from packages.utils.images import find_images_by_direction


class Rigidbody(ABC):
    """
    A class for controlling the movement
    of the game object in Pygame.
    """

    def __init__(self) -> None:
        self.__idle_position_up = find_images_by_direction(Direction.UP)
        self.__idle_position_down = find_images_by_direction(Direction.DOWN)
        self.__idle_position_left = find_images_by_direction(Direction.LEFT)
        self.__idle_position_right = find_images_by_direction(Direction.RIGHT)

        self.__run_position_up = find_images_by_direction(
            Direction.UP, range(3, 5)
        )
        self.__run_position_down = find_images_by_direction(
            Direction.DOWN, range(3, 5)
        )
        self.__run_position_left = find_images_by_direction(
            Direction.LEFT, range(3, 5)
        )
        self.__run_position_right = find_images_by_direction(
            Direction.RIGHT, range(3, 5)
        )

        self.is_acceleration = False

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def toggle_acceleration(self):
        if self.is_acceleration:
            self.is_acceleration = False
        else:
            self.is_acceleration = True

        return self.is_acceleration
