import json
import requests
from pprint import pprint
def find_mismatched_data(url, file_name):
    response = requests.get(url)
    api_data = response.json()['results']
    with open(file_name, 'r') as file:
        file_data = json.load(file)['results']

    mismatched = {}
    for api_planet, file_planet in zip(api_data, file_data):
        planet_name = api_planet['name']
        planet_mismatched = {}

        for key in file_planet.keys():
            if key not in api_planet:
                planet_mismatched[key] = {'Expected': file_planet[key], 'Actual': None}
            elif file_planet[key] != api_planet[key]:
                planet_mismatched[key] = {'Expected': file_planet[key], 'Actual': api_planet[key]}

        if planet_mismatched:
            mismatched[planet_name] = planet_mismatched

    return mismatched

if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"
    pprint(find_mismatched_data(url, file_name))
