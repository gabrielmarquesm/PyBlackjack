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
        self.round: int = 0
        self.deck: Deck = Deck()
        self.dealer: Dealer = Dealer(self.deck, Hand())
        self.player: Player = Player(STARTING_MONEY, self.deck, Hand())

    def generate_table_info(self) -> str:
        return f"Dealer's Hand:\n{self.dealer.hand}\nYour Hand:\n{self.player.hand}"

    def generate_round_info(self, bet: int) -> str:
        return f"Round {self.round} Starting!\nCash: ${self.player.cash}\nBet Amount: ${bet}"

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

    def start(self) -> None:
        print(GameStatus.GAME_START)
        input(GameStatus.WAITING_INPUT)

        while self.player.cash:
            self.start_round()

        clear_screen()
        print(GameStatus.GAME_OVER)
        print(f"Total rounds played: {self.round}.")
        input(GameStatus.WAITING_INPUT)

    def start_round(self):
        self.round += 1
        round_status: RoundStatus = RoundStatus.IN_PROGRESS

        self.dealer.clear_table(self.player)
        self.dealer.deal_initial_cards(self.player)

        clear_screen()

        bet: int = get_valid_bet(self.player.cash)

        self.generate_round_info(bet)

        if self.player.hand.points == MAX_HAND_POINTS:
            round_status = RoundStatus.BLACKJACK

        while round_status == RoundStatus.IN_PROGRESS:
            clear_screen()
            action: PlayerAction = get_player_action(self.generate_table_info())
            round_status = self.handle_player_action(PlayerAction(action))

        clear_screen()
        self.player.update_cash(bet, round_status)
        print(round_status)
        print(self.generate_table_info())

        input(GameStatus.WAITING_INPUT)

    def prepare_round(self):
        # self.round += 1
        # round_status: RoundStatus = RoundStatus.IN_PROGRESS
        # self.dealer.clear_table(self.player)
        # self.dealer.deal_initial_cards(self.player)
        pass

    def end_round(self):
        # clear_screen()
        # self.player.update_cash(bet, round_status)
        # print(round_status)
        # print(self.generate_table_info())
        pass
