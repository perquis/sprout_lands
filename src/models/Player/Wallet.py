from abc import ABC


class Wallet(ABC):
    def __init__(self) -> None:
        self.__wallet: float = 0.0

    def get_wallet(self):
        return self.__wallet

    def manage_pocket(self, money: float):
        self.__wallet += money

    def spend_pocket(self, money: float):
        self.__wallet -= money

        if self.__wallet < 0:
            self.__wallet = 0
