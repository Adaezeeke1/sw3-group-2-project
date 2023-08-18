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
- Create a new file called utilities.py
- Create a variable called API_KEY and assign your API key (as a string) to this variable. 
- For example, your utilities.py file should look like this:

    API_KEY = "CopyYourAPIKeyHere"

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
![image](https://github.com/Adaezeeke1/sw3-group-2-project/blob/main/UML.jpg)
