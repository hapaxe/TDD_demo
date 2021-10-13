from PySide2.QtWidgets import QApplication, QPushButton, QWidget
from PySide2 import QtWidgets

from src.domain.ports.basket_port import AbstractBasket


class AuthUI(QWidget, AbstractBasket):
    def __init__(self, amount):
        # documentation
        # explaining
        super(QWidget).__init__()
        self.ok_button = QPushButton()
        self.amount = amount

    def get_amount(self) -> int:
        return self.amount
