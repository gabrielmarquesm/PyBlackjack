from enum import Enum
import os


STARTING_MONEY: int = 1000
MAX_HAND_POINTS: int = 21

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


class Suit(str, Enum):
    """Suits in a standard deck of playing cards."""

    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"


class PlayerAction(str, Enum):
    """Player actions in a round."""

    HIT = "1"
    STAND = "2"


class RoundStatus(str, Enum):
    """Status of a round in a game."""

    BLACKJACK = "Blackjack! You won the round."
    WIN = "You won the round."
    TIE = "Tie."
    LOSE = "You lose the round."
    IN_PROGRESS = "Round in progress."

    def __str__(self) -> str:
        return self.value


class GameStatus(str, Enum):
    """Overall status of a game."""

    START = "Welcome to PyBlackjack!"
    RESTART = "Do you want to restart the game? (y/n): "
    GAME_OVER = "Game over!"
    WAITING_INPUT = "Press any key to continue..."
    INVALID_INPUT = "Invalid input. Please enter 'y' or 'n'."

    def __str__(self) -> str:
        return self.value


def clear_screen() -> None:
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_bet(cash: int) -> int:
    """Get a valid bet amount from the user (Positive integer less than total cash)."""
    while True:
        try:
            print(f"Cash: ${cash}")
            bet: int = int(input("Bet Amount: "))

            if bet <= 0:
                clear_screen()
                print("Please enter a positive integer.")

            elif bet > cash:
                clear_screen()
                print("Bet amount exceeds available cash. Please enter a valid bet.")
            else:
                return bet
        except ValueError:
            clear_screen()
            print("Enter a valid bet amount.")


def get_player_action(game_info: str) -> PlayerAction:
    """Get the player action (HIT or STAND)"""
    while True:
        print(game_info)
        action: str = input("Actions:\n1 - HIT\n2 - STAND\nSELECT:")
        if action == PlayerAction.HIT or action == PlayerAction.STAND:
            return PlayerAction(action)
        else:
            clear_screen()
            print("Invalid action. Please choose 1 for HIT or 2 for STAND.")
