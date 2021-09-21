import requests
import logging
import pickle

from constants import api_key, api_token, todo_list_id, annatasks_list_id

base_url = 'https://api.trello.com/1/'

logging.basicConfig(filename='exceptions.log', level=logging.INFO)

for id, name in zip([todo_list_id, annatasks_list_id], ['todo', 'anna']):
    try:
        url = base_url + f'/lists/{id}/cards?key={api_key}&token={api_token}'
        response = requests.get(url)
        response.raise_for_status()    
    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.info(f'Other error occurred: {err}')

    with open(f'latest-{name}.pkl', 'wb') as f:
        pickle.dump(response.json(), f)