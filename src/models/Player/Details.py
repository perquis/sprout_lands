from abc import ABC
from datetime import datetime


class Details(ABC):
    def __init__(self) -> None:
        self.__days: int = 0
        self.created_at = datetime.now()
        self.updated_at = None

    def add_day(self):
        self.__days += 1
