from flask import Flask, render_template, request, redirect, url_for
from feminist_heroes_class import FeministHeroesVsChallenges
import random

app = Flask(__name__)


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
    try:
        choice = request.form["choice"]
    except KeyError:
        choice = "0"
    game.player_card = game.player.cards[int(choice)]
    game.choose_card(int(choice))
    return render_template("battle.html", player_card=game.player_card, challenge_card=game.challenge_card)


@app.route("/results", methods=["POST", "GET"])
def results():
    try:
        chosen_attribute_hashed = request.form["attribute"]
    except KeyError:
        chosen_attribute = random.choice(list(game.challenge_card.attributes.keys()))
    else:
        chosen_attribute = chosen_attribute_hashed.replace("#", " ")
    finally:
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

@app.route("/restart", methods=["POST"])
def restart_game():
    game.reset()
    return redirect(url_for('home'))


if __name__ == "__main__":
    game = FeministHeroesVsChallenges()
    app.run(debug=True)


game = FeministHeroesVsChallenges()