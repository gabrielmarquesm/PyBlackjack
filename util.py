from enum import Enum
from os import name, system


STARTING_MONEY: int = 1000
MAX_HAND_POINTS: int = 21


class Suit(str, Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"


class PlayerAction(str, Enum):
    HIT = "1"
    STAND = "2"


class RoundStatus(str, Enum):
    BLACKJACK = "Blackjack! You won the round"
    WIN = "You won the round"
    TIE = "Tie"
    LOSE = "You lose the round"
    IN_PROGRESS = "Round in progress"

    def __str__(self) -> str:
        return self.value


class GameStatus(str, Enum):
    GAME_START = "Welcome to PyBlackjack!"
    GAME_OVER = "Game over!"
    WAITING_INPUT = "Press any key to continue..."

    def __str__(self) -> str:
        return self.value


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


def clear_screen() -> None:
    system("cls" if name == "nt" else "clear")


def get_positive_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                raise ValueError("Enter a valid number.")
        except ValueError:
            print("Enter a valid number.")


def get_valid_bet_amount(cash: int) -> int:
    while True:
        try:
            print(f"Cash: ${cash}")
            bet: int = get_positive_integer_input("Bet Amount: ")
            if bet > cash:
                print("You don't have enough cash for this bet.")
            else:
                return bet
        except ValueError:
            print("Enter a valid bet amount.")
            clear_screen()


def get_player_action(game_info: str) -> PlayerAction:
    while True:
        print(game_info)

        action: str = input("Actions:\n1 - HIT\n2 - STAND\nSELECT:")
        if action == PlayerAction.HIT or action == PlayerAction.STAND:
            return PlayerAction(action)
        else:
            print("Invalid action. Please choose 1 for HIT or 2 for STAND.")
            clear_screen()
