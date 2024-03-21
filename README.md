# PyBlackjack
A text-based Blackjack game implemented in Python using object-oriented programming principles. Play against an automated dealer, place bets, and enjoy the thrill of the casino right from your terminal!

### Setting Up:
- The game begins by prompting the player to enter their initial amount of money.
- The player is then asked to place their bet for the current round.

### Dealing Cards:
- The dealer deals two cards to the player, both face up.
- The dealer deals two cards to themselves, one face up and one face down.

### Player's Turn:
- The player decides whether to 'hit' (request another card) or 'stand' (keep their current hand).
- If the player's total hand value exceeds 21 ('busts'), they lose the round immediately.

### Dealer's Turn:
- Once the player stands, the dealer reveals their face-down card.
- The dealer must 'hit' (take additional cards) until their hand value is 17 or more.

### Determining the Winner:
- If neither the player nor the dealer busts, the hand with the highest total value wins.
- If the player's total is higher than the dealer's, the player wins and receives their bet back plus an equal amount from the dealer.
- If the dealer's total is higher than the player's, the player loses their bet.
- If both the player and the dealer have the same total, it's a tie ('push') and the player gets their bet back.

### Updating Money:
- After each round, the player's total money is adjusted based on the outcome (win, loss, or tie).

### Continuing or Quitting:
- After each round, the player can choose to continue playing or quit the game.
- If the player runs out of money, the game ends automatically.
