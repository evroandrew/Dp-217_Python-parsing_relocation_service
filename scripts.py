import requests
import re


def compare(first:str, second:str) -> bool:
    pattern = r'[\s!.,\\|/_\-*%$#@]+'
    first = re.sub(pattern, '', first.lower())
    second = re.sub(pattern, '', second.lower())
    return ((first == second) or (first in second) or (second in first))


def get_data_from(url:str) -> dict:
    data = requests.get(url).json()
    # print(data, type(data))
    return data


def merge_similar(housings:list) -> list:
    """Removes repeated"""
    return housings


def parse_2gis(city:str) -> list:
    url = f'https://catalog.api.2gis.com/3.0/items?city_id=141373143515660&key=YOUR_KEY'  # https://www.booking.com/
    data = get_data_from(url).get('result', {}).get('items', [])
    housings = []
    for hid in data:
        housings.append({
            'type': data[hid].get('type', 0), 
            'address': data[hid].get('address_name', ''), 
            'phone': data[hid].get('phone', ''), 
            'uni': data[hid].get('university_name', ''),
        })
    return housings


def parse(city:str) -> list:
    housings = []
    housings.extend(parse_2gis(city))
    return housings
