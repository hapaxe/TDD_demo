import abc


class AbstractBasket(metaclass=abc.ABCMeta):
    def get_amount(self) -> int:
        raise NotImplementedError
