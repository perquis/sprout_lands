from uuid import uuid4
from packages.enums import Gender, Type


from packages.models.Player.Account import Account
from packages.models.Player.Details import Details
from packages.models.Player.Level import Level


class Player(Account, Details, Level):
    """
    Represents a player model in a game.
    """

    instances = 0
    id: str = uuid4()

    def __init__(self, nickname: str, gender: Gender) -> None:
        super().__init__()
        self.nickname = nickname
        self.gender = gender
        self.type = Type.Player
        self.equipment: list = []

        Player.instances += 1

    def __str__(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        return self.type == other.type


print()
