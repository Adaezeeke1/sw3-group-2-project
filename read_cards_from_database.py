import mysql.connector

from card_class import Card

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Zxy005676!',
    database='top_trumps'
)
cursor = connection.cursor()


# Function to fetch cards from the database
def fetch_cards():
    cursor.execute('SELECT Cards.name, Categories.name, Attributes.name, Card_Attribute_Score.score FROM Cards \
                    JOIN Categories ON Cards.category_id = Categories.id \
                    JOIN Card_Attribute_Score ON Cards.id = Card_Attribute_Score.card_id \
                    JOIN Attributes ON Card_Attribute_Score.attribute_id = Attributes.id')

    cards = {}
    for row in cursor.fetchall():
        card_name, category, attribute_name, score = row
        if card_name not in cards:
            cards[card_name] = {
                'category': category,
                'attributes': {},
            }
        cards[card_name]['attributes'][attribute_name] = score

    return cards


# Fetch cards from the database
cards_data = fetch_cards()

# Transform data into Card objects
cards = []
for card_name, card_data in cards_data.items():
    category = card_data['category']
    attribute_names = list(card_data['attributes'].keys())
    attribute_scores = card_data['attributes']

    card = Card(card_name, attribute_names, attribute_scores, category)
    cards.append(card)

# Close the database connection
connection.close()

'''
# Print the fetched cards
for card in cards:
    print("Card:", card.name)
    print("Category:", card.category)
    print("Attribute Names:", card.attribute_names)
    print("Attribute Scores:", card.attribute_scores)
    print()
'''
