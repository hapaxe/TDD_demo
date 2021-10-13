import unittest

from test.unit_tests.stubbasket import StubBasket
from src.domain.exceptions import NotEnoughMoneyError
from src.domain.user import User


class TestTransaction(unittest.TestCase):
    def test_transaction_goes_well(self):
        # given
        user = User()
        user.account = 30
        # when
        basket = StubBasket(20)
        user.buy(basket)
        # then
        self.assertEqual(user.account, 10)

    def test_transaction_goes_well2(self):
        # given
        user = User()
        user.account = 40
        # when
        basket = StubBasket(20)
        user.buy(basket)
        # then
        self.assertEqual(user.account, 20)

    def test_not_enough_money_on_account(self):
        # given
        user = User()
        user.account = 10
        # when
        basket = StubBasket(20)
        with self.assertRaises(NotEnoughMoneyError):
            user.buy(basket)
        self.assertEqual(user.account, 10)


if __name__ == '__main__':
    unittest.main()
