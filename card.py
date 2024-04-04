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
        self.hidden: bool = False

    def hide(self) -> None:
        self.hidden = True

    def reveal(self) -> None:
        self.hidden = False

    def __str__(self) -> str:
        if self.hidden:
            return "Hidden Card"

        return f"{self.rank_name.capitalize()} of {self.suit.value}"
