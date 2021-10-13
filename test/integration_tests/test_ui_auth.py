import unittest
from PySide2.QtWidgets import QApplication

from src.adapters.auth_ui import AuthUI


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # runs only once before the tests are being run
        app = QApplication()

    def setUp(self) -> None:
        # runs once before EACH test
        pass

    def test_auth_goes_right_if_user_exists(self):
        # given
        ui = AuthUI(20)
        # when
        ui.first_name = "Alex"
        ui.last_name = "Corrales"
        ui.ok_button.click()
        # then
        self.assertEqual(ui.amount, 20)

    def test_auth_goes_right_if_user_exists_other_amount(self):
        # given
        ui = AuthUI(300000000)
        # when
        ui.first_name = "Alex"
        ui.last_name = "Fremaux"
        ui.ok_button.click()
        # then
        self.assertEqual(ui.amount, 300000000)


if __name__ == '__main__':
    unittest.main()
