from PySide2.QtWidgets import QApplication, QPushButton, QWidget
from PySide2 import QtWidgets


class AuthUI(QWidget):
    def __init__(self, amount):
        super(QWidget).__init__()
        self.ok_button = QPushButton()
        self.amount = amount
