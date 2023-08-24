import unittest

from player_deck import PlayerDeck
import requests


class TestPlayerDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.player_deck = PlayerDeck()

    def test_generate_player_cards(self):
        # To test if the player cards are generated correctly and to check the number of player cards
        player_cards = self.player_deck.generate_player_cards()
        self.assertEqual(len(player_cards), 4) 


def test_generate_player_cards_with_mock(self):
    # To test the generate_player_cards method using a mock for the fetch_quote.
    with patch.object(Card, 'fetch_quote') as mock_fetch_quote:
        mock_fetch_quote.return_value = "Test Quote"
        player_cards = self.player_deck.generate_player_cards()

# Check number of player cards.
    self.assertEqual(len(player_cards), 4)  
    for card in player_cards:
        self.assertEqual(card.quote, "Test Quote")  


if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
 unittest.main()


