import unittest

from src.domain.badge import Badge
from src.domain.basket import Basket
from src.domain.user import User


class MyTestCase(unittest.TestCase):

    def test_badge_condition(self):
        # given
        user = User()
        user.account = 150
        # when
        basket = Basket(100)
        user.buy(basket)
        # then
        badge = Badge()
        self.assertEqual(user.badges, [badge])


if __name__ == '__main__':
    unittest.main()
