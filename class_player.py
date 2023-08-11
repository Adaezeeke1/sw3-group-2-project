class Player:
    def __init__(self, player_deck):
        self.cards = player_deck.cards

    def draw_card(self, card):
        self.cards.append(card)