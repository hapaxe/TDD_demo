import unittest
from PySide2.QtWidgets import QApplication

from src.adapters.auth_ui import AuthUI


class MyTestCase(unittest.TestCase):

    def test_auth_goes_right_if_user_exists(self):
        # given
        app = QApplication()
        ui = AuthUI(20)
        # when
        ui.first_name = "Alex"
        ui.last_name = "Corrales"
        ui.ok_button.click()
        # then
        self.assertEqual(ui.amount, 20)

    def test_auth_goes_right_if_user_exists(self):
        # given
        app = QApplication()
        ui = AuthUI(300000000)
        # when
        ui.first_name = "Alex"
        ui.last_name = "Fremaux"
        ui.ok_button.click()
        # then
        self.assertEqual(ui.amount, 300000000)


if __name__ == '__main__':
    unittest.main()
