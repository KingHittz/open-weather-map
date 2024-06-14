#Made by. Justin Turner 11:33AM 4/25/24

import datetime
import requests

class WeatherData:
    def __init__(self, api_key, city, state):
        self.api_key = api_key
        self.city = city
        self.state = state
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather?'

    def get_weather(self):
        url = f"{self.base_url}appid={self.api_key}&q={self.city}"
        response = requests.get(url).json()
        return self.pull_data(response)

    def pull_data(self, data):
        temp_kelvin = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'])
        return {
            'temp_kelvin': temp_kelvin,
            'feels_like_kelvin': feels_like_kelvin,
            'wind_speed': wind_speed,
            'humidity': humidity,
            'description': description,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time
        }

    def convert_kelvin_to_celsius_fahrenheit(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

def main():
    api_key = 'b9f3269290ef5f9e7de33a3db53afbf6'  # Replace with your actual API key
    city = 'Manchester'
    state = 'Tennessee'

    weather = WeatherData(api_key, city, state)
    data = weather.get_weather()

    celsius, fahrenheit = weather.convert_kelvin_to_celsius_fahrenheit(data['temp_kelvin'])

    print(f'Sun rises in {city}, {state} at {data["sunrise_time"]}) local time.')
    print(f'Sun sets in {city}, {state} at {data["sunset_time"]}) local time.')
    print(f'Wind speed in {city}, {state}: {data["wind_speed"]} m/s')
    # You can add similar print statements for other data points

main()

