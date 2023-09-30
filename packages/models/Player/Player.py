from uuid import uuid4
from packages.models.Player import *
from packages.enums import *


class Player(Level, Account, Details, Equipment, Rigidbody):
    """
    Represents a player model in a game.
    """

    instances = 0
    id: str = uuid4()

    def __init__(self, nickname: str, gender: Gender) -> None:
        super(Level, self).__init__()
        super(Account, self).__init__()
        super(Details, self).__init__()
        super(Equipment, self).__init__()
        super(Rigidbody, self).__init__()
        self.nickname = nickname
        self.type = Type.Player
        self.gender = gender

        Player.instances += 1

    def __str__(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        return self.type == other.type
