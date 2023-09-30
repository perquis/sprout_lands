from abc import ABC


class Level(ABC):
    def __init__(self) -> None:
        self.__level: int = 1

    def level_up(self):
        """
        Level up a character by adding experience
        points.
        """
        self.__level += 1
