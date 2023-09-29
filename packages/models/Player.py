from uuid import uuid4
from pygame import Rect
from datetime import datetime

from packages import resources
from packages.enums import Gender, Type


class Player:
    players = 0
    id: str = uuid4()

    def __init__(self, nickname: str, gender: Gender) -> None:
        # private
        self.__days: int = 0
        self.__level: int = 1

        # public
        self.nickname = nickname
        self.gender = gender
        self.type = Type.Player
        self.equipment: list = []
        self.created_at = datetime.now()
        self.updated_at = None

        Player.players += 1

    def __str__(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        return self.type == other.type

    def get_level(self) -> int:
        return self.level

    def get_nickname(self) -> str:
        return self.nickname

    def add_day(self):
        self.__days += 1

    def level_up(self):
        self.__level += 1

    @property
    def rigidbody(self, filename) -> Rect:
        return resources.character(self.filename)


p = Player("perquis", Gender.MALE)
