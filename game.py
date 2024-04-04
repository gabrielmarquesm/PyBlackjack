from dealer import Dealer
from deck import Deck
from hand import Hand
from player import Player
from util import (
    STARTING_MONEY,
    MAX_HAND_POINTS,
    GameStatus,
    PlayerAction,
    RoundStatus,
    clear_screen,
    get_player_action,
    get_valid_bet,
)


class Game:
    def __init__(self) -> None:
        self.current_round: int
        self.round_status: RoundStatus
        self.deck: Deck
        self.dealer: Dealer
        self.player: Player

    def start(self) -> None:
        while True:
            self.current_round = 0
            self.deck = Deck()
            self.dealer = Dealer(self.deck, Hand())
            self.player = Player(STARTING_MONEY, self.deck, Hand())

            print(GameStatus.START)
            input(GameStatus.WAITING_INPUT)

            while self.player.cash:
                self.prepare_round()
                clear_screen()
                self.play_round()

            clear_screen()

            print(GameStatus.GAME_OVER)
            print(f"Total rounds played: {self.current_round}.")

            if not self.restart():
                break

            clear_screen()

    def restart(self) -> None | bool:
        while True:
            answer: str = input(GameStatus.RESTART).strip().lower()
            if answer == "y":
                return True
            if answer == "n":
                return False

            clear_screen()
            print(GameStatus.INVALID_INPUT)

    def prepare_round(self) -> None:
        self.current_round += 1
        self.round_status: RoundStatus = RoundStatus.IN_PROGRESS
        self.dealer.clear_table(self.player)
        self.dealer.deal_initial_cards(self.player)

    def play_round(self) -> None:
        bet: int = get_valid_bet(self.player.cash)
        self.generate_round_info(bet)

        if self.player.hand.points == MAX_HAND_POINTS:
            self.round_status = RoundStatus.BLACKJACK

        while self.round_status == RoundStatus.IN_PROGRESS:
            clear_screen()
            action: PlayerAction = get_player_action(self.generate_table_info())
            self.round_status = self.handle_player_action(PlayerAction(action))

        clear_screen()
        self.player.update_cash(bet, self.round_status)

        print(self.generate_round_result())
        input(GameStatus.WAITING_INPUT)

    def handle_player_action(self, action: PlayerAction) -> RoundStatus:
        match action:
            case PlayerAction.HIT:
                self.player.hit()
                if self.player.hand.points == MAX_HAND_POINTS:
                    self.dealer.reveal_card()
                    if self.dealer.hand.points == MAX_HAND_POINTS:
                        return RoundStatus.TIE
                    else:
                        return RoundStatus.BLACKJACK

                elif self.player.hand.points > MAX_HAND_POINTS:
                    self.dealer.reveal_card()
                    return RoundStatus.LOSE

                else:
                    return RoundStatus.IN_PROGRESS

            case PlayerAction.STAND:
                self.dealer.reveal_card()
                self.dealer.hit()

                if self.dealer.hand.points == self.player.hand.points:
                    return RoundStatus.TIE

                elif self.dealer.hand.points > MAX_HAND_POINTS:
                    return RoundStatus.WIN

                elif self.dealer.hand.points < self.player.hand.points:
                    return RoundStatus.WIN

                else:
                    return RoundStatus.LOSE

    def generate_table_info(self) -> str:
        return f"Dealer's Hand:\n{self.dealer.hand}\nYour Hand:\n{self.player.hand}"

    def generate_round_info(self, bet: int) -> str:
        return f"Round {self.current_round} Starting!\nCash: ${self.player.cash}\nBet Amount: ${bet}"

    def generate_round_result(self) -> str:
        return f"{self.round_status}\n{self.generate_table_info()}"
