import random


class Card:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


class Artist:
    def __init__(self):
        self.cards = [
            Card("Beyonce", {'singing voice': 10, 'creativity': 7, 'painting': 0, 'composing': 3}),
            Card("Frida Kahlo", {'singing voice': 2, 'creativity': 10, 'painting': 10, 'composing': 2})
        ]


class Hero:
    def __init__(self):
        self.cards = [
            Card("Wonder Woman", {'strength': 9, 'speed': 10, 'courage': 7, 'resilience': 5}),
            Card("lady deadpool", {'strength': 7, 'speed': 5, 'courage': 10, 'resilience': 2})
        ]


class Academic:
    def __init__(self):
        self.cards = [
            Card("Ruth Bader Ginsburg", {'intelligence': 9, 'political influence': 9, 'determination': 6, 'rebellious': 7}),
            Card("Hypatia", {'intelligence': 10, 'political influence': 3, 'determination': 9, 'rebellious': 10})
        ]


class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)


class FeministHeroesVsChallenges:
    def __init__(self):
        # Initialize player and challenge decks with cards
        self.player_deck = Deck("Player Deck", self.generate_player_cards())
        self.challenge_deck = Deck("Challenge Cards", [
            Card("Make the world better with music", {'singing voice': 8, 'creativity': 5, 'composing': 4}),
            Card("Justice System needs reform!", {'intelligence': 6, 'political influence': 7, 'rebellious': 8}),
            Card("Women can be Heroes", {'strength': 8, 'speed': 8, 'courage': 6})
        ])

        self.player_score = 0

    def generate_player_cards(self):
        player_cards = []
        classes = [Artist(), Hero(), Academic()]
        for _ in range(4):
            player_class = random.choice(classes)
            card = random.choice(player_class.cards)
            player_cards.append(card)
        return player_cards

    def show_cards(self):
        # Display the player's cards to choose from
        print("Your cards:")
        for i, card in enumerate(self.player_deck.cards, 1):
            print(f"{i}. {card.name}")

    def choose_card(self):
        # Player chooses a card to play from their deck
        self.show_cards()
        choice = int(input("Choose the card you will use for this challenge (1-4): ")) - 1
        return self.player_deck.cards.pop(choice)

    def play_round(self):
        # Display the challenge card attributes
        challenge_card = self.challenge_deck.draw()
        print("New Round!")
        print(f"Challenge: {challenge_card.name}")
        print("Challenge attributes:")
        for attribute, value in challenge_card.attributes.items():
            print(f"{attribute}: {value}")



        # Player chooses a card to play
        player_card = self.choose_card()

        # Player chooses an attribute to challenge
        attribute_choice = input("Choose an attribute to challenge: ")


        # Check if the player card has the chosen attribute
        if attribute_choice not in player_card.attributes:
            print("You lose the round! Your card does not have the chosen attribute.")
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

    def play_game(self):
        # Welcome message and deck shuffling
        print("Welcome to Feminist Heroes vs. Challenges!")
        self.player_deck.shuffle()

        while len(self.player_deck.cards) > 0:
            # Main game loop - continue playing until the player's deck runs out of cards
            challenge_card = self.challenge_deck.draw()

            # Play the round
            self.play_round()

        # Game over - determine the winner based on the player's score
        if self.player_score > 0:
            print("Congratulations! You defeated the challenges and made the world a better place!")
        else:
            print("The challenges have proven to be tough. Keep striving for progress!")


if __name__ == "__main__":
    game = FeministHeroesVsChallenges()
    game.play_game()