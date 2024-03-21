from card import Card


class Hand:
    def __init__(self):
        self.cards: list[Card] = []
        self.points = 0

    def add_card(self, card):
        self.cards.append(card)
        self.points += card.points

    # if points + ace > 21 then ace = 1 else ace = 11.
    def adjust_for_ace(self):
        pass
