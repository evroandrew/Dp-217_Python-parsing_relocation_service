import requests
import os


def parse_from_api() -> list:
    url = os.environ.get('HOUSING_API_URL')
    querystring = {"query":'ukraine', "locale":"uk"}
    headers = {
        'x-rapidapi-host': os.environ.get('HOUSING_API_HOST'),
        'x-rapidapi-key': os.environ.get('HOUSING_API_KEY'),
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    housings = response.text.get('items', [])
    return housings


def parse() -> list:
    housings = yield parse_from_api()
    return housings
