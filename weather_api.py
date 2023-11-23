import json
import requests
from typing import Final

from model import Weather, dt

# constants
API_KEY: Final[str] = 'cb75949cfaffb088b942355d27e779fd'
BASAE_URL: Final[str] = 'http://api.openweathermap.org/data/2.5/forecast'

def get_weather(city_name, mock:bool = False) -> dict:
    """ Gets the current wewather form the weather api"""

    # return dummy data for testing
    if mock:
        print('Using mock data..')
        with open('dummy_data.json') as file:
            return json.load(file)
        
    # request live data
    payload: dict = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url=BASAE_URL, params=payload)
    data: dict = request.json()

    # write the data into json file
    with open('dummy_data.json', 'w') as file:
        json.dump(data, file) 

    return data

def get_weather_details(weather: dict) -> list[Weather]:
    """ takes the weather json and turns into a nice list of Weather objects"""

    days: list[dict] = weather.get('list')

    # if there is no data for days, no point in continuing
    if not days:
        raise Exception(f'[rpblem in json: {weather}]')
    
    # Try to add the info we want to our list_of_weather
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description'))
        list_of_weather.append(w)

    return list_of_weather
