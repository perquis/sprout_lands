from uuid import UUID, uuid4

import pygame as pg

from packages.enums import *
from packages.models.Player import *


class Player(Level, Account, Details, Equipment, Rigidbody):
    """
    Represents a player model in a game.
    """

    id: UUID = uuid4()

    def __init__(self, nickname: str, speed: float) -> None:
        pg.sprite.Sprite.__init__(self)
        super(Level, self).__init__()
        super(Account, self).__init__()
        super(Details, self).__init__()
        super(Equipment, self).__init__(speed=speed)
        super(Rigidbody, self).__init__()
        self.nickname = nickname
        self.type = Type.Player
