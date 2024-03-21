from card import Card
from hand import Hand


class Player:
    def __init__(self, cash: int, hand: Hand) -> None:
        self.cash: int = cash
        self.hand: Hand = hand

    def hit(self):
        pass

    def guard(self):
        pass
