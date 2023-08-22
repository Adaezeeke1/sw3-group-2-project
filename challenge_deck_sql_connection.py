import random
import mysql.connector
from card_class import Card
from config import challenge_db_config

class ChallengeDeck:
    def __init__(self, database_path):
        self.database_path = database_path
        self.cards = []
        self.load_cards()
        self.shuffle()

    def load_cards(self):
        with mysql.connector.connect(**self.database_path) as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT card_id, name, image FROM Cards")  # Adjust the query to fetch card names and images
            rows = cursor.fetchall()
            for row in rows:
                card_id, card_name, card_image = row['card_id'], row['name'], row['image']
                attributes = self.load_attributes_for_card(card_id, connection)
                self.cards.append(Card(card_name, card_image, attributes, None))  # Assuming Card class accepts name, image, attributes, and quote

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


    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

# db_config = {
#     'host': '127.0.0.1',
#     'user': 'root',
#     'password': 'Jgm1fdopsw',
#     'database': 'challenge_cards'
# }

# # Creates an instance of the ChallengeDeck class
# challenge_deck = ChallengeDeck(db_config)
#
# # Simulates drawing cards from the challenge deck
# while True:
#     card = challenge_deck.draw()
#     if card is None:
#         print("No more cards in the challenge deck.")
#         break
#     print(f"Drawn card: {card}")
#     print(f"Drawn card name: {card.name}")
#     print(f"Drawn card image: {card.image}")
#     print(f"Drawn card attributes: {card.attributes}")