from random import shuffle
from .card import Card
from .util import Suit, RANK


class Deck:

    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.build()
        self.shuffle()

    def build(self) -> None:
        self.cards = [Card(suit, name) for suit in Suit for name in RANK]

    def shuffle(self) -> None:
        shuffle(self.cards)

    def deal(self) -> Card:
        if not self.cards:
            self.build()
            self.shuffle()
        return self.cards.pop()
