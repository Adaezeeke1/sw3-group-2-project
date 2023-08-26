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
- Copy your API key into the variable called API_KEY (inside the speech marks)."

## Running the program:
- On main.py click 'run'
- After a few seconds, you should see this line on the terminal:
    Running on http://127.0.0.1:5000
- Go to your browser, type localhost:5000 and click enter.

## Set up
pip install mysql-connector-python  
pip install requests  
## System design
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/system%20design.png)

## UML Diagram
This is our data model.
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/UML%20for%20challenge_cards.jpg)
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/UML%20for%20player_cards.jpg)
**Disciption:**
1. **Categories:**
    - This table is intended to store different categories that cards can belong to.
    - The primary purpose of this table is to provide a way to categorize cards, making it easier to organize and retrieve them.
2. **Attributes:**
    - This table is used to store different attributes that can be associated with cards.
    - Attributes could represent characteristics of the cards
3. **Cards:**
    - This table stores information on the cards.
    - The **`category_id`** column references the **`category_id`** from the Categories table, indicating the category to which the card belongs, allowing efficient categorization and retrieval of cards.
4. **Card_Attribute_Score:**
    - This table is designed to store attribute scores for each card.
    - It uses composite foreign keys: **`card_id`** references the Cards table and **`attribute_id`** references the Attributes table.
    - This table enables you to associate attributes with cards and assign scores to these attributes on a per-card basis.

**Reasons for this Data Model Design:**

1. The design helps in reducing data redundancy and maintaining data integrity. Each table serves a specific purpose, and data is organized efficiently.
2. The use of foreign keys establishes relationships between tables, enabling to retrieve related data easily and ensuring referential integrity.
3. This design allows for easy addition of new categories, attributes, and cards without requiring major changes to the schema.

