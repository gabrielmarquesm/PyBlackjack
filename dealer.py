from card import Card
from deck import Deck
from hand import Hand
from player import Player


class Dealer:

    def __init__(self, deck: Deck, hand: Hand) -> None:
        self.deck: Deck = deck
        self.hand: Hand = hand

    def deal_initial_cards(self, player: Player):
        for _ in range(2):
            card: Card = self.deck.deal()
            player.hand.add_card(card)

        for _ in range(2):
            card: Card = self.deck.deal()
            self.hand.add_card(card)

    def reveal_card(self):
        pass
