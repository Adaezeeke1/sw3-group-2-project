import unittest
from project_knowledge import get_quote
from main import PlayerDeck, FeministHeroesVsChallenges


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


if __name__ == '__main__':
    unittest.main()
