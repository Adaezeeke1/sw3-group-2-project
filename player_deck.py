import random
from card_class import Card
class PlayerDeck:
    def __init__(self):
        self.categories = {
            "Artist": [
                Card("Beyonce", "beyonce.png", {'Singing Voice': 10, 'Creativity': 7, 'Painting': 0, 'Composing': 5}),
                Card("Sinead O'Connor", "placeholder.png", {'Singing Voice': 9, 'Creativity': 8, 'Painting': 0, 'Composing': 8}),
                Card("Frida Kahlo", "frida.png", {'Singing Voice': 2, 'Creativity': 10, 'Painting': 10, 'Composing': 2}),
                Card("Taylor Swift", "placeholder.png", {'Singing Voice': 8, 'Creativity': 10, 'Painting': 2, 'Composing': 9}),
            ],
            "Actors": [
                Card("Penelope Cruz", "placeholder.png", {'Acting': 8, 'Comedy': 7, 'Charisma': 9, 'Confidence': 9}),
                Card("Susan Sarandon", "placeholder.png", {'Acting': 9, 'Comedy': 8, 'Charisma': 7, 'Confidence': 7}),
                Card("Whoopi Goldberg", "placeholder.png", {'Acting': 8, 'Comedy': 9, 'Charisma': 8, 'Confidence': 10}),
                Card("Meryl Streep", "placeholder.png", {'Acting': 10, 'Comedy': 6, 'Charisma': 9, 'Confidence': 8}),
            ],
            "Academic": [
                Card("Ruth Bader Ginsburg", "ruth.jpg",
                     {'Intelligence': 9, 'Political Influence': 9, 'Determination': 6, 'Rebellious': 9}),
                Card("Hypatia", "placeholder.png", {'Intelligence': 10, 'Political Influence': 3, 'Determination': 9, 'Rebellious': 10}),
                Card("Rosa Parks", "rosa.jpg", {'Intelligence': 8, 'Courage': 10, 'Resilience': 9, 'Rebellious': 10}),
            ],
            "Activist": [
                Card("Florence Given", "placeholder.png", {'Confidence': 10, 'Activism': 10, 'Empowerment': 9, 'Social Influence': 8}),
                Card("Emily Pankhurst", "pankhurst.jpg", {'Confidence': 9, 'Activism': 10, 'Leadership': 10, 'Inspiration': 8}),
                Card("Malala Yousafzai", "malala.jpg", {'Confidence': 6, 'Activism': 10, 'Leadership': 10, 'Inspiration': 10}),
            ],
            "Scientist": [
                Card("Ada Lovelace", "ada.jpg", {'Intelligence': 10, 'Mathematics': 9, 'Creativity': 8, 'Logic': 10}),
                Card("Marie Curie", "placeholder.png", {'Intelligence': 9, 'Science': 10, 'Chemistry': 10, 'Physics': 9}),
                Card("Mamie Phipps Clark", "mamie.jpg", {'Intelligence': 9, 'Psychology': 10, 'Research': 8, 'Empowerment': 7}),
                Card("Maria Telkes", "placeholder.png", {'Intelligence': 9, 'Science': 10, 'Solar Energy': 10, 'Innovation': 8}),
                Card("Beatrice Shilling", "placeholder.png", {'Intelligence': 9, 'Engineering': 10, 'Innovation': 9, 'Resilience': 8}),
            ],
            "Politician": [
                Card("Michelle Obama", "michelle.jpg",
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