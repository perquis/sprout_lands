from abc import ABC


class Equipment(ABC):
    def __init__(self) -> None:
        self.equipment: list = []
