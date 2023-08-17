import unittest
from main import FeministHeroesVsChallenges, PlayerDeck
from project_knowledge import get_quote

class TestGetQuote(unittest.TestCase):
    def test_get_quote(self):
        quote = get_quote("Marilyn Monroe")
        self.assertIsNotNone(quote)


class TestPlayerDeck(unittest.TestCase):
    def setUp(self):
        self.player_deck = PlayerDeck()

    def test_generate_player_cards(self):
        player_cards = self.player_deck.generate_player_cards()
        self.assertEqual(len(player_cards), 4)


class TestEndGameStatus(unittest.TestCase):
    def setUp(self):
        self.game = MockFeministHeroesVsChallenges()

    def test_player_win_status(self):
        self.game.player_score = 3
        self.game.computer_score = 2
        status = FeministHeroesVsChallenges.check_win(self.game)
        self.assertEqual(status, "Congratulations! You defeated the challenges and made the world a better place!")

    def test_computer_win_status(self):
        self.game.player_score = 2
        self.game.computer_score = 3
        status = FeministHeroesVsChallenges.check_win(self.game)
        self.assertEqual(status, "The challenges have proven to be tough. Keep striving for progress!")

    def test_tie_status(self):
        self.game.player_score = 2
        self.game.computer_score = 2
        status = FeministHeroesVsChallenges.check_win(self.game)
        self.assertEqual(status, "It's a tie! The battle was intense, but there's still more to conquer!")

class TestAttributeComparison(unittest.TestCase):

    def setUp(self):
        self.game = MockFeministHeroesVsChallenges()
    def test_player_score_higher(self):
        player_card = MockCard(name = None, attributes={'Singing Voice': 10, 'Creativity': 7, 'Painting': 0, 'Composing': 5})
        challenge_card = MockCard(name = None, attributes = {'Singing Voice': 8, 'Creativity': 5, 'Composing': 4})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice = "Creativity")
        self.assertEqual("Your Creativity of 7 is higher than 5. You win the round!", result)

    def test_player_score_lower(self):
        player_card = MockCard(name=None, attributes={'Acting': 10, 'Comedy': 6, 'Charisma': 9, 'Confidence': 8})
        challenge_card = MockCard(name= None, attributes={'Acting': 7, 'Charisma': 8, 'Comedy': 7})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice = "Comedy")
        self.assertEqual("Your Comedy of 6 is lower than 7. You lose the round!", result)


    # Let's change the message here to be that the numbers are equal and you win. As it is, it says the number is higher and it's not true.
    def test_scores_equal(self):
        challenge_card = MockCard(name = None, attributes = {'Resilience': 7, 'Determination': 9, 'Confidence': 6} )
        player_card = MockCard(name= None, attributes={'Confidence': 6, 'Activism': 10, 'Leadership': 10, 'Inspiration': 10})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice="Confidence")
        self.assertEqual("Your Confidence of 6 is higher than 6. You win the round!", result)

    def test_attribute_not_in_player_card(self):
        challenge_card = MockCard(name=None, attributes={'Political Influence': 8, 'Social Influence': 8, 'Activism': 7})
        player_card = MockCard(name= None, attributes={'Physical Fitness': 9, 'Determination': 9, 'Resilience': 8, 'Confidence': 8})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice="Social Influence")
        self.assertEqual("You lose the round! Your card does not have the Social Influence attribute.", result)

class TestCardChoice(unittest.TestCase):
    def setUp(self):
        self.game = FeministHeroesVsChallenges()
        self.game.player.cards = [MockCard("Card 1", None), MockCard("Card 2", None)]

    def test_card_choice(self):
        chosen_card = self.game.choose_card(1)
        self.assertEqual(chosen_card.name, "Card 2")

class MockFeministHeroesVsChallenges:
    def __init__(self):
        self.player_deck = None
        self.player = None
        self.challenge_deck = None
        self.player_score = 0
        self.computer_score = 0
class MockCard:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


if __name__ == '__main__':
    unittest.main()