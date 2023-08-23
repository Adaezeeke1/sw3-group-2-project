import mysql.connector
from card_class import Card
from config import player_db_config
import json

def insert_new_card(conn, category, card_name, card_image):
    cursor = conn.cursor()

    # Check if the category exists
    cursor.execute("SELECT category_id FROM categories WHERE name = %s", (category,))
    category_id = cursor.fetchone()

    if category_id is None:
        # If category doesn't exist, insert it
        cursor.execute("INSERT INTO categories (name) VALUES (%s)", (category,))
        conn.commit()
        category_id = cursor.lastrowid  # This will have the auto-generated category_id

    # Insert the card
    cursor.execute("INSERT INTO cards (category_id, name, image) VALUES (%s, %s, %s)", (category_id, card_name, card_image))
    conn.commit()

    cursor.close()
    print("Card added successfully!")

def upsert_attributes_by_card_name(conn, card_name, attributes):
    cursor = conn.cursor()

    # Check if the category exists
    cursor.execute("SELECT card_id FROM cards WHERE name = %s", (card_name,))
    card_id = cursor.fetchone()
    if card_id is None:
        print("card name not exist, you need to add new card using option 1")
    else:
        for attribute_name, score in attributes.items():
            # Check if the attribute exists
            cursor.execute("SELECT attribute_id FROM Attributes WHERE name = %s", (attribute_name,))
            attribute_id = cursor.fetchone()

            if attribute_id is None:
                # Insert attribute if it doesn't exist
                cursor.execute("INSERT INTO Attributes (name) VALUES (%s)", (attribute_name,))
                attribute_id = cursor.lastrowid
            else:
                attribute_id = attribute_id[0]
            # Upsert into Card_Attribute_Score
            upsert_query = """
                INSERT INTO Card_Attribute_Score (card_id, attribute_id, score)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE score = VALUES(score)
            """
            cursor.execute(upsert_query, (card_id[0], attribute_id, score))

            # Commit changes and close the connection
        conn.commit()
        cursor.close()
        print("Attributes added successfully!")

def main():
    while True:
        print("Options:")
        print("1. Add a new card")
        print("2. Add new attributes to a card")
        print("3. Quit")
        option = int(input("Choose an option: "))
        conn = mysql.connector.connect(**player_db_config)
        if option == 1:
            category = input("Enter category: ")
            card_name = input("Enter card name: ")
            card_image = input("Enter card image: ")
            # Insert new card and handle category
            insert_new_card(conn, category, card_name, card_image)
        elif option == 2:
            card_name = input("Enter card name: ")
            attributes = input("Enter attributes with dictionary format({\"attribute_name:score\"}): ")
            try:
                attributes_dict = json.loads(attributes)
                # Upsert Card_Attribute_Score and handle attributes
                upsert_attributes_by_card_name(conn, card_name, attributes_dict)
            except json.JSONDecodeError as e:
                print("Invalid input format. Please use a dictionary as input")
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a valid option.")
        conn.close()


if __name__ == "__main__":
    main()