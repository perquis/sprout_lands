from abc import ABC


class Equipment(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.equipment: list = []
