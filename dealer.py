from deck import Deck
from hand import Hand
from player import Player


class Dealer:

    def __init__(self, deck: Deck, hand: Hand) -> None:
        self.deck: Deck = deck
        self.hand: Hand = hand

    def deal_initial_cards(self, player: Player) -> None:
        for _ in range(2):
            self.hand.add_card(self.deck.deal())
            player.hand.add_card(self.deck.deal())

        self.hand.cards[0].hide()

    def reveal_card(self) -> None:
        self.hand.cards[0].reveal()

    def hit(self) -> None:
        while self.hand.points < 17:
            self.hand.add_card(self.deck.deal())

    def clear_table(self, player: Player):
        self.hand.clear()
        player.hand.clear()
