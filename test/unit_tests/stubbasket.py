from src.domain.ports.basket_port import AbstractBasket


class StubBasket(AbstractBasket):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self) -> int:
        return self.__amount
