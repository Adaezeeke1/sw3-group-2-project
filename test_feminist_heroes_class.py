import unittest
from feminist_heroes_class import FeministHeroesVsChallenges
from project_knowledge import get_quote
from player_deck_sql_connection import PlayerDeck
from player_deck_sql_connection import player_db_config
from challenge_deck_sql_connection import ChallengeDeck
from challenge_deck_sql_connection import challenge_db_config
from card_class import Card

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


class TestPlayerDeck(unittest.TestCase):
    def setUp(self):
        self.player_deck = PlayerDeck(player_db_config)

    def test_player_deck_setup(self):
        self.assertIsInstance(self.player_deck, PlayerDeck)
        self.assertIsNotNone(self.player_deck.database_path)
        self.assertIsNotNone(self.player_deck.categories)
        self.assertIsNotNone(self.player_deck.cards)

    def test_load_categories(self):
        categories = self.player_deck.load_categories()
        self.assertEqual(len(categories), 7)

    def test_generate_player_cards(self):
        player_cards = self.player_deck.generate_player_cards()
        self.assertEqual(len(player_cards), 4)

class TestCardClass(unittest.TestCase):
    def setUp(self):
        self.card = Card("Meryl Streep", "test.jpg", {"attribute": 2}, None)

    def test_card_initalisation(self):
        self.assertIsInstance(self.card, Card)
        self.assertEqual(self.card.name, "Meryl Streep")
        self.assertEqual(self.card.image, "test.jpg")
        self.assertEqual(self.card.attributes, {"attribute": 2})
        self.assertIsNone(self.card.quote)

class TestChallengeDeck(unittest.TestCase):

    def setUp(self):
        self.challenge_deck = ChallengeDeck(challenge_db_config)

    def test_challenge_deck_setup(self):
        self.assertIsInstance(self.challenge_deck, ChallengeDeck)
        self.assertIsNotNone(self.challenge_deck.database_path)
        self.assertIsNotNone(self.challenge_deck.cards)

    def test_draw_card(self):
        initial_length = len(self.challenge_deck.cards)
        self.challenge_deck.draw()
        length_after_draw = len(self.challenge_deck.cards)
        self.assertEqual(initial_length - 1, length_after_draw)

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
