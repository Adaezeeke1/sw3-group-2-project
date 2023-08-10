import random
from project_knowledge import get_quote
from flask import Flask, render_template, request

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

    def choose_card(self, choice):
        return self.player.cards.pop(choice)
    def compare_attributes(self, attribute_choice):
        if attribute_choice not in self.player_card.attributes:
            result = f"You lose the round! Your card does not have the {attribute_choice} attribute."
            self.computer_score += 1
            return result
        else:
            player_attribute_value = self.player_card.attributes[attribute_choice]
            challenge_attribute_value = self.challenge_card.attributes[attribute_choice]
            if player_attribute_value >= challenge_attribute_value:
                result = f"Your {attribute_choice} of {player_attribute_value} is higher than " \
                         f"{challenge_attribute_value}. You win the round!"
                self.player_score += 1
                return result
            else:
                result = f"Your {attribute_choice} of {player_attribute_value} is lower than " \
                         f"{challenge_attribute_value}. You lose the round!"
                self.computer_score += 1
                return result
    def get_quote(self):
        if self.player_card.quote:
            return f"{self.player_card.name}'s quote: {self.player_card.quote}"
        else:
            return f"{self.player_card.name} has no available quote"

    def check_win(self):
        if self.player_score > self.computer_score:
            return "Congratulations! You defeated the challenges and made the world a better place!"
        elif self.computer_score > self.player_score:
            return "The challenges have proven to be tough. Keep striving for progress!"
        else:
            return "It's a tie! The battle was intense, but there's still more to conquer!"
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/submit/", methods=["POST", "GET"])
def choose_cards():
    game.challenge_deck.shuffle()
    game.challenge_card = game.challenge_deck.draw()
    length = len(game.player.cards)
    return render_template("choose_cards.html", player_cards=game.player.cards,
                           challenge_card=game.challenge_card, length = length)

@app.route("/battle", methods=["POST", "GET"])
def battle():
    choice = request.form["choice"]
    game.player_card = game.player.cards[int(choice)]
    game.choose_card(int(choice))
    return render_template("battle.html", player_card = game.player_card, challenge_card = game.challenge_card)

@app.route("/results", methods = ["POST", "GET"])
def results():
    chosen_attribute_hashed = request.form["attribute"]
    chosen_attribute = chosen_attribute_hashed.replace("#", " ")
    print(chosen_attribute)
    results = game.compare_attributes(chosen_attribute)
    quote = game.get_quote()
    player_card_length = len(game.player.cards)
    challenge_card_length = len(game.challenge_deck.cards)
    return render_template("result.html", player_card=game.player_card, challenge_card=game.challenge_card,
                           results = results, player_score = game.player_score,
                           computer_score = game.computer_score, quote = quote,
                           player_card_length = player_card_length, challenge_card_length = challenge_card_length)

@app.route("/end", methods = ["POST", "GET"])
def end_game():
    win_status = game.check_win()
    return render_template("end.html", win_status = win_status,
                           computer_score = game.computer_score, player_score = game.player_score)

if __name__ == "__main__":
    game = FeministHeroesVsChallenges()
    # game.play_game()
    app.run(debug=True)