import unittest
from card_class import Card
class TestCardClass(unittest.TestCase):
    def setUp(self):
        self.card = Card("Meryl Streep", "test.jpg", {"attribute": 2}, None)

    def test_card_initalisation(self):
        self.assertIsInstance(self.card, Card)
        self.assertEqual(self.card.name, "Meryl Streep")
        self.assertEqual(self.card.image, "test.jpg")
        self.assertEqual(self.card.attributes, {"attribute": 2})
        self.assertIsNone(self.card.quote)