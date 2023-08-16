import unittest
from unittest.mock import patch

import main
from main import FeministHeroesVsChallenges
from card_class import Card

class TestAttributeComparison(unittest.TestCase):
    def test_player_score_higher(self):
        player_card = Card(name = "Beyonce", image = "beyonce.png", attributes={'Singing Voice': 10, 'Creativity': 7, 'Painting': 0, 'Composing': 5})
        challenge_card = Card(name = "Make the world better with music", image = "music.jpg", attributes = {'Singing Voice': 8, 'Creativity': 5, 'Composing': 4})
        game = FeministHeroesVsChallenges()
        game.player_card = player_card
        game.challenge_card = challenge_card
        expected = "Your Creativity of 7 is higher than 5. You win the round!"
        result = FeministHeroesVsChallenges.compare_attributes(game, attribute_choice = "Creativity")
        self.assertEqual(expected, result)

    def test_player_score_lower(self):
        player_card = Card(name="Meryl Streep", image="streep.jpg", attributes={'Acting': 10, 'Comedy': 6, 'Charisma': 9, 'Confidence': 8})
        challenge_card = Card(name="Take centre stage", image="stage.jpg", attributes={'Acting': 7, 'Charisma': 8, 'Comedy': 7})
        game = FeministHeroesVsChallenges()
        game.player_card = player_card
        game.challenge_card = challenge_card
        expected = "Your Comedy of 6 is lower than 7. You lose the round!"
        result = FeministHeroesVsChallenges.compare_attributes(game, attribute_choice = "Comedy")
        self.assertEqual(expected, result)


    # Let's change the message here to be that the numbers are equal and you win. As it is, it says the number is higher and it's not true. 
    def test_scores_equal(self):
        challenge_card = Card(name = "Never give up", image = "nevergiveup.jpg", attributes = {'Resilience': 7, 'Determination': 9, 'Confidence': 6} )
        player_card = Card(name="Malala Yousafzai", image="malala.jpg", attributes={'Confidence': 6, 'Activism': 10, 'Leadership': 10, 'Inspiration': 10})
        game = FeministHeroesVsChallenges()
        game.player_card = player_card
        game.challenge_card = challenge_card
        expected = "Your Confidence of 6 is higher than 6. You win the round!"
        result = FeministHeroesVsChallenges.compare_attributes(game, attribute_choice="Confidence")
        self.assertEqual(expected, result)

    def test_attribute_not_in_player_card(self):
        challenge_card = Card(name="Change minds, Change Lives", image="influence.jpg", attributes={'Political Influence': 8, 'Social Influence': 8, 'Activism': 7})
        player_card = Card(name="Serena Williams", image="serenawilliams.jpeg", attributes={'Physical Fitness': 9, 'Determination': 9, 'Resilience': 8, 'Confidence': 8})
        game = FeministHeroesVsChallenges()
        game.player_card = player_card
        game.challenge_card = challenge_card
        expected = "You lose the round! Your card does not have the Social Influence attribute."
        result = FeministHeroesVsChallenges.compare_attributes(game, attribute_choice="Social Influence")
        self.assertEqual(expected, result)

class TestWinLoseTie(unittest.TestCase):
    def test_tie(self):
        FeministHeroesVsChallenges.player_score = 0
        FeministHeroesVsChallenges.computer_score = 0
        expected = "It's a tie! The battle was intense, but there's still more to conquer!"
        result = FeministHeroesVsChallenges.check_win(FeministHeroesVsChallenges)
        self.assertEqual(expected, result)

    def test_player_win(self):
        FeministHeroesVsChallenges.player_score = 3
        FeministHeroesVsChallenges.computer_score = 1
        expected = "Congratulations! You defeated the challenges and made the world a better place!"
        result = FeministHeroesVsChallenges.check_win(FeministHeroesVsChallenges)
        self.assertEqual(expected, result)

    def test_computer_win(self):
        FeministHeroesVsChallenges.player_score = 2
        FeministHeroesVsChallenges.computer_score = 4
        expected = "The challenges have proven to be tough. Keep striving for progress!"
        result = FeministHeroesVsChallenges.check_win(FeministHeroesVsChallenges)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()