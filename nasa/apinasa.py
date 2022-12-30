import json
import requests

api_token = 'XEbehRgBHtf4jLYOcVLQmL0Ywk7RqOxemSj7NXKO'
api_url = 'https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY'


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
