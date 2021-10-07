from .badge import Badge
from .exceptions import NotEnoughMoneyError


class User:
    def __init__(self):
        badge = Badge()
        self.badges = [badge]
        self.account = 0

    def buy(self, basket):
        if basket.amount > self.account:
            raise NotEnoughMoneyError
        self.account -= basket.amount
