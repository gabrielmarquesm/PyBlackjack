from .deck import Deck
from .hand import Hand
from .util import RoundStatus


class Player:
    def __init__(self, cash: int, deck: Deck, hand: Hand) -> None:
        self.cash: int = cash
        self.deck: Deck = deck
        self.hand: Hand = hand

    def hit(self) -> None:
        self.hand.add_card(self.deck.deal())

    def update_cash(self, bet: int, round_result: RoundStatus) -> None:
        if bet > 0:
            if round_result == RoundStatus.WIN or round_result == RoundStatus.BLACKJACK:
                self.cash += bet
            elif round_result == RoundStatus.LOSE:
                self.cash -= bet
