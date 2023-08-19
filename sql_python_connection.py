import mysql.connector
from card_class import Card
import random
from config import db_config

class DbConnectionError(Exception):
    pass

class PlayerDeck:
    def __init__(self, database_path):
        self.database_path = database_path
        self.categories = self.load_categories()
        self.cards = self.generate_player_cards()

    def load_categories(self):
        categories = {}
        with mysql.connector.connect(**self.database_path) as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT category_id, name FROM Categories")  # Change 'id' to 'category_id'
            rows = cursor.fetchall()
            for row in rows:
                category_id, category_name = row['category_id'], row['name']
                categories[category_name] = self.load_cards_by_category(category_id, connection)
        return categories

    def load_cards_by_category(self, category_id, connection):
        cards = []
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT card_id, name, image FROM Cards WHERE category_id = %s", (category_id,))
        rows = cursor.fetchall()
        for row in rows:
            card_id, card_name, card_image = row['card_id'], row['name'], row['image']
            attributes = self.load_attributes_for_card(card_id, connection)
            cards.append(Card(card_name, card_image, attributes))
        cursor.close()
        return cards

    def load_attributes_for_card(self, card_id, connection):
        attributes = {}
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT a.name AS attribute_name, ca.score FROM Attributes a JOIN Card_Attribute_Score ca ON a.attribute_id = ca.attribute_id WHERE ca.card_id = %s",
            (card_id,))

        rows = cursor.fetchall()
        for row in rows:
            attributes[row['attribute_name']] = row['score']
        cursor.close()
        return attributes

    def generate_player_cards(self):
        player_cards = []
        while len(player_cards) < 4 and any(self.categories.values()):
            category = random.choice(list(self.categories.keys()))
            if self.categories[category]:
                card = random.choice(self.categories[category])
                card.fetch_quote()  # Implement this method to fetch the quote for the card
                player_cards.append(card)
                self.categories[category].remove(card)
        return player_cards



