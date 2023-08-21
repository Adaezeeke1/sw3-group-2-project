import mysql.connector


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Omoyemhe.1',
    'database': 'player_cards'
}

connection = mysql.connector.connect(**db_config)

cursor = connection.cursor()

# Example query to fetch data from the table
query = "SELECT * FROM attributes"
cursor.execute(query)
attributes = cursor.fetchall()

for attribute in attributes:
    print(attribute)

cursor.close()
connection.close()

# Added details to help with sql setup
