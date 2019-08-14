from src.oystercard.exceptions.fare_excpetion import CustomFareException


class Card(object):

    def __init__(self):
        self._balance = 0.0

    def set_balance(self, money):
        self._balance = money

    def get_balance(self):
        return self._balance

    def check_limit(self, fare):
        if self._balance < fare:
            raise CustomFareException("Don't have enough money, you need to top up your card")

    def go_out(self, fare):
        self.check_limit(fare)
        self._balance = self._balance - fare
        return self

    def go_in(self, fare):
        self._balance = self._balance + fare
        return self

    def top_up(self, money):
        self._balance = self._balance + money
        return self
