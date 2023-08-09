import random
from project_knowledge import get_quote
from flask import Flask, render_template

app = Flask(__name__)
class Card:
    def __init__(self, name, attributes, quote=None):
        self.name = name
        self.attributes = attributes
        self.quote = quote

    def fetch_quote(self):
        self.quote = get_quote(self.name)

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


class Player:
    def __init__(self, player_deck):
        self.cards = player_deck.cards

    def draw_card(self, card):
        self.cards.append(card)

class ChallengeDeck:
    def __init__(self):
        self.cards = [
            Card("Make the world better with music", {'Singing Voice': 8, 'Creativity': 5, 'Composing': 4}, None),
            Card("Justice System needs reform!", {'Intelligence': 6, 'Political Influence': 7, 'Rebellious': 8}, None),
            Card("Women can be Heroes", {'Strength': 8, 'Speed': 8, 'Courage': 6}, None),
            Card("Mathematical mind", {'Intelligence': 8, 'Good at maths': 10, 'Research': 6}, None)
        ]
        # fetching quote to apply to card
        self.fetch_quotes()
        self.shuffle()

    def fetch_quotes(self):
        for card in self.cards:
            card.fetch_quote()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)


class FeministHeroesVsChallenges:
    def __init__(self):
        self.player_deck = PlayerDeck()
        self.player = Player(self.player_deck)
        self.challenge_deck = ChallengeDeck()
        self.player_score = 0
        self.computer_score = 0


    def show_cards(self, cards):
        # Display the cards to choose from
        print("Cards:")
        for i, card in enumerate(cards, 1):
            print(f"{i}. {card.name}")

    def choose_card(self):
        self.show_cards(self.player.cards)
        choice = int(input("Choose a card (1-4): ")) - 1
        return self.player.cards.pop(choice)

    def play_round(self):
        challenge_card = self.challenge_deck.draw()
        print("\nNew Round!")
        print(f"Challenge: {challenge_card.name}")
        print("Challenge attributes:")
        for attribute, value in challenge_card.attributes.items():
            print(f"{attribute}: {value}")

        player_card = self.choose_card()

        attribute_choice = input("Choose an attribute to challenge: ")

        # Check if the player card has the chosen attribute
        if attribute_choice not in player_card.attributes:
            print("You lose the round! Your card does not have the chosen attribute.")

            if player_card.quote:
                print(f"\n{player_card.name}'s quote: {player_card.quote}")
            else:
                print(f"\n{player_card.name} has no available quote")
            return

        # Compare the chosen attribute between player and challenge cards
        player_attribute_value = player_card.attributes[attribute_choice]
        challenge_attribute_value = challenge_card.attributes[attribute_choice]

        print(f"Your {attribute_choice}: {player_attribute_value}")
        print(f"Challenge {attribute_choice}: {challenge_attribute_value}")

        if player_attribute_value >= challenge_attribute_value:
            # Player wins the round
            print("You win the round!")
            self.player_score += 1
        else:
            # Player loses the round
            print("You lose the round!")

        # Display quote of the player's chosen card
        if player_card.quote:
            print(f"\n{player_card.name}'s quote: {player_card.quote}")
        else:
            print(f"\n{player_card.name} has no available quote")

    def play_game(self):
        # Welcome message and deck shuffling
        print("Welcome to Feminist Heroes vs. Challenges Battle!")
        self.player_deck.cards = self.player_deck.generate_player_cards()

        self.challenge_deck.shuffle()

        while len(self.player.cards) > 0 and len(self.challenge_deck.cards) > 0:
            self.play_round()

        # Game over - determine the winner based on scores
        print("\nBattle Over!")
        print(f"Your score: {self.player_score}")
        print(f"Computer's score: {self.computer_score}")

        if self.player_score > self.computer_score:
            print("Congratulations! You defeated the challenges and made the world a better place!")
        elif self.player_score < self.computer_score:
            print("The challenges have proven to be tough. Keep striving for progress!")
        else:
            print("It's a tie! The battle was intense, but there's still more to conquer!")


@app.route("/")
def home():
    game.challenge_deck.shuffle()
    return render_template("index.html")

@app.route("/submit/", methods=["POST", "GET"])
def choose_cards():
    game.challenge_card = game.challenge_deck.draw()
    return render_template("choose_cards.html", player_cards=game.player.cards, challenge_card=game.challenge_card)


if __name__ == "__main__":
    game = FeministHeroesVsChallenges()
    # game.play_game()
    app.run(debug=True)