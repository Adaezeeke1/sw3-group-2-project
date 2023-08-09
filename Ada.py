import random


class Card:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


class Player:
    def __init__(self):
        self.cards = []

    def draw_card(self, card):
        self.cards.append(card)


class ChallengeDeck:
    def __init__(self):
        self.cards = [
            Card("Make the world better with music", {'Singing Voice': 8, 'Creativity': 5, 'Composing': 4}),
            Card("Justice System needs reform!", {'Intelligence': 6, 'Political Influence': 7, 'Rebellious': 8}),
            Card("Women can be Heroes", {'Strength': 8, 'Speed': 8, 'Courage': 6})
        ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)


class FeministHeroesVsChallenges:
    def __init__(self):
        self.player = Player()
        self.challenge_deck = ChallengeDeck()
        self.player_score = 0
        self.computer_score = 0

    def generate_player_cards(self):
        # Create categories with their respective cards
        categories = {
            "Artist": [
                Card("Beyonce", {'Singing Voice': 10, 'Creativity': 7, 'Painting': 0, 'Composing': 5}),
                Card("Frida Kahlo", {'Singing Voice': 2, 'Creativity': 10, 'Painting': 10, 'Composing': 2})
            ],
            "Hero": [
                Card("Wonder Woman", {'Strength': 9, 'Speed': 10, 'Courage': 7, 'Resilience': 5}),
                Card("Lady Deadpool", {'Strength': 7, 'Speed': 5, 'Courage': 10, 'Resilience': 2})
            ],
            "Academic": [
                Card("Ruth Bader Ginsburg", {'Intelligence': 9, 'Political Influence': 9, 'Determination': 6, 'Rebellious': 9}),
                Card("Hypatia", {'Intelligence': 10, 'Political Influence': 3, 'Determination': 9, 'Rebellious': 10})
            ]
        }

        player_cards = []
        remaining_categories = list(categories.keys())
        while len(player_cards) < 4 and remaining_categories:
            category = random.choice(remaining_categories)
            card = random.choice(categories[category])
            player_cards.append(card)
            categories[category].remove(card)
            if not categories[category]:
                remaining_categories.remove(category)

        return player_cards

    def show_cards(self, cards):
        # Display the cards to choose from
        print("Cards:")
        for i, card in enumerate(cards, 1):
            print(f"{i}. {card.name}")

    def choose_card(self):
        # Player chooses a card to play from their deck
        self.show_cards(self.player.cards)
        choice = int(input("Choose a card (1-4): ")) - 1
        return self.player.cards.pop(choice)

    def play_round(self, player_card, challenge_card):
        # Compare the attributes between player and challenge cards
        for attribute, value in challenge_card.attributes.items():
            print(f"\nYour {attribute}: {player_card.attributes.get(attribute, 0)}")
            print(f"Challenge {attribute}: {value}")

            if player_card.attributes.get(attribute, 0) < value:
                # Player loses the round
                print("\nYou lose the round!")
                self.computer_score += 1
                return

        # Player wins the round
        print("\nYou win the round!")
        self.player_score += 1

    def play_game(self):
        # Welcome message and deck shuffling
        print("Welcome to Feminist Heroes vs. Challenges Battle!")
        self.player.cards = self.generate_player_cards()
        self.challenge_deck.shuffle()

        while len(self.player.cards) > 0 and len(self.challenge_deck.cards) > 0:
            # Draw a challenge card
            challenge_card = self.challenge_deck.draw()
            print("\nNew Round!")
            print(f"Challenge: {challenge_card.name}")
            print("Challenge attributes:")
            for attribute, value in challenge_card.attributes.items():
                print(f"{attribute}: {value}")

            # Player chooses a card to play
            player_card = self.choose_card()

            # Play the round
            self.play_round(player_card, challenge_card)

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


if __name__ == "__main__":
    game = FeministHeroesVsChallenges()
    game.play_game()