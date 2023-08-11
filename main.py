from flask import Flask, render_template, request
from class_player import Player
from player_deck import PlayerDeck
from challenge_deck import ChallengeDeck

app = Flask(__name__)


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
                           challenge_card=game.challenge_card, length=length)


@app.route("/battle", methods=["POST", "GET"])
def battle():
    choice = request.form["choice"]
    game.player_card = game.player.cards[int(choice)]
    game.choose_card(int(choice))
    return render_template("battle.html", player_card=game.player_card, challenge_card=game.challenge_card)


@app.route("/results", methods=["POST", "GET"])
def results():
    chosen_attribute_hashed = request.form["attribute"]
    chosen_attribute = chosen_attribute_hashed.replace("#", " ")
    print(chosen_attribute)
    results = game.compare_attributes(chosen_attribute)
    quote = game.get_quote()
    player_card_length = len(game.player.cards)
    challenge_card_length = len(game.challenge_deck.cards)
    return render_template("result.html", player_card=game.player_card, challenge_card=game.challenge_card,
                           results=results, player_score=game.player_score,
                           computer_score=game.computer_score, quote=quote,
                           player_card_length=player_card_length, challenge_card_length=challenge_card_length)


@app.route("/end", methods=["POST", "GET"])
def end_game():
    win_status = game.check_win()
    return render_template("end.html", win_status=win_status,
                           computer_score=game.computer_score, player_score=game.player_score)


if __name__ == "__main__":
    game = FeministHeroesVsChallenges()
    app.run(debug=True)
