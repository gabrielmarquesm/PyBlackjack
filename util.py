from enum import Enum
from os import system, name


def clear_screen() -> None:
    system("cls" if name == "nt" else "clear")


class Suit(str, Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"


class PlayerAction(str, Enum):
    HIT = "1"
    STAND = "2"


RANK: dict[str, int] = {
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "TEN": 10,
    "JACK": 10,
    "QUEEN": 10,
    "KING": 10,
    "ACE": 11,
}
