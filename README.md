# sw3-group-2-project

## API key:

To run this program, you will need to generate your own API key for the Google Knowledge Graph API.

### Creating an API key:

- First, create a Google Cloud Platform Project (https://console.cloud.google.com)
- Go into the project and, using the sidebar, navigate to 'APIs and Services > Library'.
- Search for the Google Knowledge Graph API, click into this and 'enable'.
- Go back to the sidebar and navigate to 'APIs and Services > Credentials' and click on 'create credentials'.
- You will be presented with your API key.
- This will also be stored in the Google Cloud Account under 'Enabled APIs and Services'.

### Adding your API key to the project:
- Navigate to the parent directory of the project (the directory that contains the main.py file).
- Go to the config.py file 
- Copy your API key into the variable called API_KEY (inside the speech marks).

## Setting up the database:
- Open MySQL (or alternative program of your choice)
- Run both of the .sql files in the SQL folder (challenge_cards.sql and player_cards.sql)
- Go to the config.py file and assign your password to the variable PASSWORD (inside the speech marks)
- In the config.py file, the default host and user has been filled out for you. Ensure that this is correct and change it if not. 

## Installing dependencies
- Use the command 'pipenv install' to install the dependencies listed in the pipfile.

## Running the program:
- On main.py click 'run'
- After a few seconds, you should see this line on the terminal:
    Running on http://127.0.0.1:5000
- Go to your browser, type localhost:5000 and click enter.

## System design
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main)

## UML Diagram
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/UML%20for%20challenge_cards.jpg)
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/UML%20for%20player_cards.jpg)

### UML Explanation

1. **Categories:** 
    - Each player card has a category that it belongs to. The categories table contains the id and name of each category. 
2. **Attributes:**
    - This attributes table stores the names of the different attributes in the game. 
    - Each player card and each challenge card contains four of these attributes.
3. **Cards:**
    - This table stores the names and images and categories for each different card.
    - The **`category_id`** column references the **`category_id`** from the Categories table, indicating the category to which the card belongs, allowing efficient categorization and retrieval of cards.
4. **Card_Attribute_Score:**
    - This table stores the attribute scores for each attribute of each card. 
    - It uses composite foreign keys: **`card_id`** references the Cards table and **`attribute_id`** references the Attributes table.
    - This table enables you to associate attributes with cards and assign scores to these attributes on a per-card basis.

**Reasons for this Data Model Design:**

1. The design helps in reducing data redundancy and maintaining data integrity. Each table serves a specific purpose, and data is organized efficiently.
2. The use of foreign keys establishes relationships between tables, enabling to retrieve related data easily and ensuring referential integrity.
3. This design allows for easy addition of new categories, attributes, and cards without requiring major changes to the schema.