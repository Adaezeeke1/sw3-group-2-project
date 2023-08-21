import unittest
from project_knowledge import get_quote
from main import app, PlayerDeck, FeministHeroesVsChallenges
from sql_python_connection import PlayerDeck
from sql_python_connection import db_config


class TestGetQuote(unittest.TestCase):
    def test_get_quote(self):
        quote = get_quote("Marilyn Monroe")
        self.assertIsNotNone(quote)


class TestPlayerDeck(unittest.TestCase):
    def setUp(self):
        self.player_deck = PlayerDeck(db_config)

    def test_generate_player_cards(self):
        player_cards = self.player_deck.generate_player_cards()
        self.assertEqual(len(player_cards), 4)


class TestEndGameStatus(unittest.TestCase):
    def setUp(self):
        self.game = FeministHeroesVsChallenges()
        self.game.player_score = 3
        self.game.computer_score = 2

    def test_player_win_status(self):
        status = self.game.check_win()
        self.assertEqual(status, "Congratulations! You defeated the challenges and made the world a better place!")

    def test_computer_win_status(self):
        self.game.player_score = 2
        self.game.computer_score = 3
        status = self.game.check_win()
        self.assertEqual(status, "The challenges have proven to be tough. Keep striving for progress!")

    def test_tie_status(self):
        self.game.player_score = 2
        self.game.computer_score = 2
        status = self.game.check_win()
        self.assertEqual(status, "It's a tie! The battle was intense, but there's still more to conquer!")


class TestCardChoice(unittest.TestCase):
    def setUp(self):
        self.game = FeministHeroesVsChallenges()
        self.game.player.cards = [MockCard("Card 1"), MockCard("Card 2")]

    def test_card_choice(self):
        chosen_card = self.game.choose_card(1)
        self.assertEqual(chosen_card.name, "Card 2")


class MockCard:
    def __init__(self, name):
        self.name = name


class TestGameInitialization(unittest.TestCase):
    def setUp(self):
        self.game = FeministHeroesVsChallenges()

    def test_player_deck_initialized(self):
        self.assertIsNotNone(self.game.player_deck)

    def test_player_initialized(self):
        self.assertIsNotNone(self.game.player)

    def test_challenge_deck_initialized(self):
        self.assertIsNotNone(self.game.challenge_deck)

    def test_player_score_initialized(self):
        self.assertEqual(self.game.player_score, 0)

    def test_computer_score_initialized(self):
        self.assertEqual(self.game.computer_score, 0)


if __name__ == '__main__':
    unittest.main()
