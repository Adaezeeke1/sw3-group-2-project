import unittest
from challenge_deck_sql_connection import ChallengeDeck
from challenge_deck_sql_connection import challenge_db_config

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