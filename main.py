from dealer import Dealer
from deck import Deck
from hand import Hand
from player import Player
from util import PlayerAction, clear_screen


def show_leaderboard(dealer: Dealer, player: Player) -> None:
    print(f"Dealer's Hand:\n{dealer.hand}\n")
    print(f"Your Hand:\n{player.hand}")


def initialize():
    pass


def choose_action():
    pass


def main() -> None:
    while True:
        clear_screen()
        print("PyBlackJack")
        cash = int(input("Starting Money: "))

        deck: Deck = Deck()
        deck.shuffle()

        dealer = Dealer(deck, Hand())
        player = Player(cash, deck, Hand())

        clear_screen()
        print("Round Starting:")
        # print(f"Cash: ${player.cash}")
        # bet = int(input("Amount to bet: "))

        dealer.deal_initial_cards(player)

        round_in_progress = True

        while round_in_progress:
            clear_screen()

            if player.hand.points == 21:
                round_in_progress = False
                print("BLACKJACK!\nYou Winned The Round\n")

            show_leaderboard(dealer, player)

            if not round_in_progress:
                break

            print("Actions")
            print("1 - HIT\n2 - STAND")
            action: str = input("Choose your action:")

            round_in_progress = True
            clear_screen()

            match action:
                case PlayerAction.HIT:
                    print("HIT")

                    player.hit()

                    if player.hand.points == 21:
                        round_in_progress = False
                        dealer.reveal_card()
                        if dealer.hand.points == 21:
                            print("Tie")
                        else:
                            print("BLACKJACK!\nYou Winned The Round")

                    elif player.hand.points > 21:
                        round_in_progress = False
                        dealer.reveal_card()
                        print("Dealer Wins The Round")

                    print("\n")
                    show_leaderboard(dealer, player)

                case PlayerAction.STAND:
                    print("STAND\n")

                    round_in_progress = False
                    dealer.reveal_card()
                    dealer.hit()

                    if dealer.hand.points == player.hand.points:
                        print("Tie")

                    elif dealer.hand.points > 21:
                        print("You Winned The Round")

                    elif dealer.hand.points < player.hand.points:
                        print("You Winned The Round")

                    elif dealer.hand.points > player.hand.points:
                        print("Dealer Wins The Round")

                    print("\n")
                    show_leaderboard(dealer, player)
                case _:
                    print("Invalid Action")

        input("Press any key to continue...")


if __name__ == "__main__":
    main()
