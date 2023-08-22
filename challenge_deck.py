import random
from card_class import Card
from read_cards_from_database import fetch_cards


class ChallengeDeck:
    def __init__(self):
        self.cards = fetch_cards()

    def fetch_quotes(self):
        for card in self.cards:
            card.fetch_quote()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

'''
        self.cards = [
            Card("Make the world better with music", ['Singing Voice', 'Creativity', 'Composing'], {'Singing Voice': 8, 'Creativity': 5, 'Composing': 4}, None),
            Card("Justice System needs reform!", {'Intelligence': 6, 'Political Influence': 7, 'Rebellious': 8}, None),
            Card("Women can be Heroes", {'Strength': 8, 'Speed': 8, 'Courage': 6}, None),
            Card("Mathematical mind", {'Intelligence': 8, 'Good at maths': 10, 'Research': 6}, None)
        ]
        # fetching quote to apply to card
        self.fetch_quotes()
        self.shuffle()
'''

