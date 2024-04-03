from random import shuffle
from card import Card
from util import Suit, RANK


class Deck:

    def __init__(self):
        self.cards: list[Card] = []
        for suit in Suit:
            for name in RANK:
                self.cards.append(Card(suit, name))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty, no more cards to deal.")
        return self.cards.pop()
