from uuid import uuid4
from datetime import datetime

from packages.enums import Gender, Type


class Player:
    """
    Represents a player model in a game.
    """

    instances = 0
    id: str = uuid4()

    def __init__(self, nickname: str, gender: Gender) -> None:
        # private
        self.__days: int = 0
        self.__level: int = 1
        self.__wallet: float = 0.0

        # public
        self.nickname = nickname
        self.gender = gender
        self.type = Type.Player
        self.equipment: list = []
        self.created_at = datetime.now()
        self.updated_at = None

        Player.instances += 1

    def __str__(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        return self.type == other.type

    def get_level(self) -> int:
        return self.level

    def get_nickname(self) -> str:
        return self.nickname

    def add_day(self):
        """
        Add one day to days.
        """
        self.__days += 1

    def level_up(self):
        """
        Level up a character by adding experience
        points.
        """
        self.__level += 1

    def manage_pocket(self, money: float):
        """
        This function enables the addition
        and subtraction of money from a wallet.
        """
        self.__wallet += money
