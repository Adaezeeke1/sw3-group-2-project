import mysql.connector
from card_class import Card
from config import db_config

class DbConnectionError(Exception):
    pass

class PlayerDeck:
    def __init__(self, database_path):
        self.database_path = database_path
        self.categories = self.load_categories()

    def load_categories(self):
        categories = {}
        with mysql.connector.connect(**self.database_path) as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, name FROM Categories")
            rows = cursor.fetchall()
            for row in rows:
                category_id, category_name = row['category_id'], row['name']
                categories[category_name] = self.load_cards_by_category(category_id, connection)
        return categories

    def load_cards_by_category(self, category_id, connection):
        cards = []
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, image FROM Cards WHERE category_id = %s", (category_id,))
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
        cursor.execute("SELECT a.name AS attribute_name, ca.score FROM Attributes a JOIN Card_Attribute_Score ca ON a.id = ca.attribute_id WHERE ca.card_id = %s", (card_id,))
        rows = cursor.fetchall()
        for row in rows:
            attributes[row['attribute_name']] = row['score']
        cursor.close()
        return attributes

# Replace with your actual database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'player_cards'
}

# Create an instance of the PlayerDeck class
player_deck = PlayerDeck(db_config)

# Access the categories and cards
for category, cards in player_deck.categories.items():
    print(f"Category: {category}")
    for card in cards:
        print(f"Card: {card.name}")
        print(f"Attributes: {card.attributes}")
        print("---")
