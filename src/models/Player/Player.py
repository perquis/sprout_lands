
from pygame.sprite import Sprite

from src.enums import *
from src.models.Player import *


class Player(Level, Wallet, Details, Equipment, Rigidbody):
    def __init__(self, nickname: str, speed: float) -> None:
        Sprite.__init__(self)
        super(Level, self).__init__()
        super(Wallet, self).__init__()
        super(Details, self).__init__()
        super(Equipment, self).__init__(speed)
        super(Rigidbody, self).__init__()
        self.nickname = nickname
        self.type = Type.Player
