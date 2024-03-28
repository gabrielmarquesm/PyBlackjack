from deck import Deck
from hand import Hand


class Player:
    def __init__(self, cash: int, deck: Deck, hand: Hand) -> None:
        self.cash: int = cash
        self.deck: Deck = deck
        self.hand: Hand = hand

    def hit(self) -> None:
        self.hand.add_card(self.deck.deal())

