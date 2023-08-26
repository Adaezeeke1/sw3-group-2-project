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
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/danielle_add_new_sys_design/system_design.png)

## UML Diagram
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/UML.jpg)
