class Card:
    def __init__(self, name, id, hp):
        self.name = name
        self.id = id
        self.hp = hp

# Define the connection details
connection = mysql.connector.connect(
    host='127.0.0.1'
    user='root',
    password='Dragonfly1@',
    database='top_trumps')

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Example query to fetch data from the table
query = "SELECT name, id, hp FROM Card"
cursor.execute(query)

# Fetch all the rows from the query result
rows = cursor.fetchall()
people_list = []
for row in rows:
    name, id, hp = row
    card = Card(name, id, hp)
    people_list.append(card)
cursor.close()
connection.close()
