import requests
from lxml import etree
import lxml.html
import math


def getWeather(city):
    try:
        api = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid=a9ebdb68b0dbf40182f5638efcca3afd')
    except:
        return
    r = api.json()
    if 'main' in r:

        temperature = math.floor(r['main']['temp'] - 273)
        feels_like = math.floor(r['main']['feels_like'] - 273)
        weather_desc = r['weather'][0]['description']
        message = f'Погода сейчас: {weather_desc}, {temperature}°C, ощущается как {feels_like}°C. Город {r["name"]}'
        print(message)
        return str(message)

    else:
        print('Not found')
        return 'Not found'
