from pygame import Rect

from packages import resources


class Player:
    def __init__(self, filename: str):
        self.filename = filename

    @property
    def rigidbody(self) -> Rect:
        return resources.character(self.filename)
