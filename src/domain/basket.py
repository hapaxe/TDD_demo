# import abc
#
#
# class AbstractBasket(metaclass=abc.ABCMeta):
#     def get_amount(self) -> int:
#         raise NotImplementedError
#
#
# class UIBasket(AbstractBasket, QWidget):
#     def __init__(self, amount):
#         super(QWidget).__init__()
#         self.amount = amount
#
#     def get_amount(self):
#         return "self.qlabelamount.value"


class Basket:
    def __init__(self, amount):
        self.amount = amount
