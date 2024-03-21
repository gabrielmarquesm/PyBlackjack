from random import shuffle
from card import Card
from util import Suit, RANK


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for name in RANK:
                self.cards.append(Card(suit, name))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
