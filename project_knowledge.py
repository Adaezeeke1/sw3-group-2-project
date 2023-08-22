import requests
from config import API_KEY

def get_quote(name):
    api_key = API_KEY
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': name,
        'limit': 1,
        'indent': True,
        'key': api_key
    }

    try:
        response = requests.get(service_url, params=params)
        data = response.json()
        if 'itemListElement' in data and len(data['itemListElement']) > 0:
            item = data['itemListElement'][0]['result']
            if 'description' in item:
                return item['description']
        return None
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return None