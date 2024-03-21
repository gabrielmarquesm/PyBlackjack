from util import Suit, RANK


class Card:

    def __init__(self, suit: Suit, rank_name: str) -> None:
        if not isinstance(suit, Suit):
            raise ValueError("Invalid suit")
        if rank_name not in RANK:
            raise ValueError("Invalid rank name")

        self.suit: Suit = suit
        self.rank_name: str = rank_name
        self.points: int = RANK[rank_name]

    def __str__(self) -> str:
        return f"{self.rank_name.capitalize()} of {self.suit.value}"
