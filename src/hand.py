from .card import Card
from .util import MAX_HAND_POINTS, RANK


class Hand:

    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.points: int = 0

    def add_card(self, card: Card) -> None:
        if card.points == RANK["ACE"]:
            self.adjust_for_ace(card)
        self.cards.append(card)
        self.points += card.points

    def adjust_for_ace(self, card: Card) -> None:
        if self.points + RANK["ACE"] > MAX_HAND_POINTS:
            card.points = 1

    def clear(self) -> None:
        self.cards = []
        self.points = 0

    def __str__(self) -> str:
        output: str = ""
        hidden_card_points: int = 0

        for card in self.cards:
            if card.hidden:
                hidden_card_points = card.points
            output += f"- {card}\n"

        output += f"Total Points: {self.points - hidden_card_points}\n"

        return output
