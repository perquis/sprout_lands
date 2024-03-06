from abc import ABC


class Account(ABC):
    def __init__(self) -> None:
        self.__wallet: float = 0.0

    def get_wallet(self):
        return self.__wallet

    def manage_pocket(self, money: float):
        """
        This function enables the addition
        and subtraction of money from a wallet.
        """
        self.__wallet += money
