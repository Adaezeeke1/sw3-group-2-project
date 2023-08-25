import unittest
from feminist_heroes_class import FeministHeroesVsChallenges
from project_knowledge import get_quote



class TestGetQuote(unittest.TestCase):
    def test_get_quote_valid_input(self):
        quote = get_quote("Marilyn Monroe")
        self.assertIsNotNone(quote)

    def test_get_quote_invalid_input(self):
        quote = get_quote("")
        self.assertIsNone(quote)

    def test_get_quote_exception_handling(self):
        with self.assertRaises(Exception):
            get_quote()

class TestGameInitialization(unittest.TestCase):
    def setUp(self):
        self.game = FeministHeroesVsChallenges()

    def test_game_initialization(self):
        self.assertIsNotNone(self.game.player_deck)
        self.assertIsNotNone(self.game.player)
        self.assertIsNotNone(self.game.challenge_deck)
        self.assertEqual(self.game.player_score, 0)
        self.assertEqual(self.game.computer_score, 0)

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
        self.assertEqual("Your Creativity of 7 is higher than the challenge score of 5. You win the round!", result)

    def test_player_score_lower(self):
        player_card = MockCard(name=None, attributes={'Acting': 10, 'Comedy': 6, 'Charisma': 9, 'Confidence': 8})
        challenge_card = MockCard(name= None, attributes={'Acting': 7, 'Charisma': 8, 'Comedy': 7})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice = "Comedy")
        self.assertEqual("Your Comedy of 6 is lower than the challenge score of 7. You lose the round!", result)
    def test_scores_equal(self):
        challenge_card = MockCard(name=None, attributes = {'Resilience': 7, 'Determination': 9, 'Confidence': 6} )
        player_card = MockCard(name=None, attributes={'Confidence': 6, 'Activism': 10, 'Leadership': 10, 'Inspiration': 10})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice="Confidence")
        self.assertEqual("Your Confidence of 6 is the same as the challenge score of 6. You win the round!", result)

    def test_attribute_not_in_player_card(self):
        challenge_card = MockCard(name=None, attributes={'Political Influence': 8, 'Social Influence': 8, 'Activism': 7})
        player_card = MockCard(name=None, attributes={'Physical Fitness': 9, 'Determination': 9, 'Resilience': 8, 'Confidence': 8})
        self.game.player_card = player_card
        self.game.challenge_card = challenge_card
        result = FeministHeroesVsChallenges.compare_attributes(self.game, attribute_choice="Social Influence")
        self.assertEqual("You lose the round! Your card does not have the Social Influence attribute.", result)

class TestCardChoice(unittest.TestCase):
    def setUp(self):
        self.player = lambda: None
        self.player.cards = [MockCard("Card 1", None), MockCard("Card 2", None)]

    def test_card_choice(self):
        chosen_card = FeministHeroesVsChallenges.choose_card(self, 1)
        self.assertEqual(chosen_card.name, "Card 2")
        self.assertEqual(len(self.player.cards), 1)

class TestReset(unittest.TestCase):

    def setUp(self):
        self.game = FeministHeroesVsChallenges()

    def test_function_initializes_game(self):
        self.game.reset()
        self.assertIsNotNone(self.game.player_deck)
        self.assertIsNotNone(self.game.player)
        self.assertIsNotNone(self.game.challenge_deck)

    def test_function_resets_scores(self):
        self.game.computer_score = 5
        self.game.player_score = 3
        self.game.reset()
        self.assertEqual(self.game.player_score, 0)
        self.assertEqual(self.game.computer_score, 0)

    def test_function_resets_decks(self):
        self.game.choose_card(0)
        self.game.challenge_deck.draw()
        challenge_deck_length_after_draw = len(self.game.challenge_deck.cards)
        self.game.reset()
        self.assertEqual(len(self.game.player_deck.generate_player_cards()), 4)
        self.assertNotEquals(challenge_deck_length_after_draw, len(self.game.challenge_deck.cards))


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
