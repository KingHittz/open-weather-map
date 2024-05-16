#Made by. Justin Turner 11:33AM 4/25/24

import datetime as datetime

import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

API_KEY = 'INSERT_API_HERE'

CITY = 'INSERT_CITY_HERE'

STATE = 'INSERT_STATE_HERE'

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = datetime.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = datetime.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f'Sun rises in {CITY, STATE} at {sunrise_time}) local time.')
print(f'Sun sets in {CITY,STATE} at {sunset_time}) local time.')
print(f'Wind speed in {CITY, STATE}: {wind_speed}m/s')
