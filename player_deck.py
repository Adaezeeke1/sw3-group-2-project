import random
from card_class import Card
class PlayerDeck:
    def __init__(self):
        self.categories = {
            "Artist": [
                Card("Beyonce", {'Singing Voice': 10, 'Creativity': 7, 'Painting': 0, 'Composing': 5}),
                Card("Sinead O'Connor", {'Singing Voice': 9, 'Creativity': 8, 'Painting': 0, 'Composing': 8}),
            ],
            "Academic": [
                Card("Ruth Bader Ginsburg",
                     {'Intelligence': 9, 'Political Influence': 9, 'Determination': 6, 'Rebellious': 9}),
                Card("Hypatia", {'Intelligence': 10, 'Political Influence': 3, 'Determination': 9, 'Rebellious': 10}),
                Card("Rosa Parks", {'Intelligence': 8, 'Courage': 10, 'Resilience': 9}),
            ],
            "Activist": [
                Card("Florence Given", {'Confidence': 10, 'Activism': 10, 'Empowerment': 9, 'Social Influence': 8}),
                Card("Emily Pankhurst", {'Confidence': 9, 'Activism': 10, 'Leadership': 10, 'Inspiration': 8}),
                Card("Malala Yousafzai", {'Confidence': 6, 'Activism': 10, 'Leadership': 10, 'Inspiration': 10}),
            ],
            "Scientist": [
                Card("Ada Lovelace", {'Intelligence': 10, 'Mathematics': 9, 'Creativity': 8, 'Logic': 10}),
                Card("Marie Curie", {'Intelligence': 9, 'Science': 10, 'Chemistry': 10, 'Physics': 9}),
                Card("Mamie Phipps Clark", {'Intelligence': 9, 'Psychology': 10, 'Research': 8, 'Empowerment': 7}),
                Card("Maria Telkes", {'Intelligence': 9, 'Science': 10, 'Solar Energy': 10, 'Innovation': 8}),
                Card("Beatrice Shilling", {'Intelligence': 9, 'Engineering': 10, 'Innovation': 9, 'Resilience': 8}),
            ],
            "Politician": [
                Card("Michelle Obama",
                     {'Intelligence': 10, 'Political Influence': 10, 'Leadership': 10, 'Empowerment': 9}),
            ],
        }

        self.cards = self.generate_player_cards()

    def generate_player_cards(self):
        player_cards = []
        while len(player_cards) < 4 and any(self.categories.values()):
            category = random.choice(list(self.categories.keys()))
            if self.categories[category]:
                card = random.choice(self.categories[category])
                card.fetch_quote()
                player_cards.append(card)
                self.categories[category].remove(card)
        return player_cards