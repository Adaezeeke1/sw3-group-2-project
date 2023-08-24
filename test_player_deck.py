import unittest
from player_deck_sql_connection import PlayerDeck
from player_deck_sql_connection import player_db_config
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

if __name__ == '__main__':
    unittest.main()