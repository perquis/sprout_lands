from abc import ABC
from datetime import datetime


class Details(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__days: int = 0
        self.created_at = datetime.now()
        self.updated_at = None

    def add_day(self):
        """
        Add one day to days.
        """
        self.__days += 1
