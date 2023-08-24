from class_player import Player
from player_deck_sql_connection import PlayerDeck
from player_deck_sql_connection import player_db_config
from challenge_deck_sql_connection import challenge_db_config
from challenge_deck_sql_connection import ChallengeDeck

class FeministHeroesVsChallenges:
    def __init__(self):
        self.player_deck = PlayerDeck(player_db_config)
        self.player = Player(self.player_deck)
        self.challenge_deck = ChallengeDeck(challenge_db_config)
        self.challenge_card = self.challenge_deck.cards[0]  # This has changed
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
                if player_attribute_value > challenge_attribute_value:
                    result = f"Your {attribute_choice} of {player_attribute_value} is higher than " \
                         f"the challenge score of {challenge_attribute_value}. You win the round!"
                elif player_attribute_value == challenge_attribute_value:
                    result = f"Your {attribute_choice} of {player_attribute_value} is the same as the challenge " \
                             f"score of {challenge_attribute_value}. You win the round!"
                self.player_score += 1
                return result
            else:
                result = f"Your {attribute_choice} of {player_attribute_value} is lower than " \
                         f"the challenge score of {challenge_attribute_value}. You lose the round!"
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

    def reset(self):
        self.player_deck = PlayerDeck(player_db_config)
        self.player = Player(self.player_deck)
        self.challenge_deck = ChallengeDeck(challenge_db_config)
        self.challenge_card = self.challenge_deck.cards[0]  # This has changed
        self.player_score = 0
        self.computer_score = 0