"""This Script is made to pull data from openweathermap"""

import datetime
import requests
from util import convert_kelvin_to_celsius_fahrenheit


class WeatherData:
    """This is the blueprint for creating objects, attributes and functionality aka methods"""

    def __init__(self, api_key, city, state):
        """This is a method which is called whenever you create a new WeatherData object, this also takes three arguments"""
        self.api_key = api_key
        self.city = city
        self.state = state
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self):
        """This method is designed to retrieve weather data for the city and state stored in the object"""
        url = f"{self.base_url}appid={self.api_key}&q={self.city}"
        response = requests.get(url, timeout=10).json()
        return self.pull_data(response)

    def pull_data(self, data):
        """This method exacts specific weather data from the provided JSON data"""
        temp_kelvin = data["main"]["temp"]
        feels_like_kelvin = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        sunrise_time = datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"] + data["timezone"]
        )
        sunset_time = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"] + data["timezone"]
        )
        return {
            """This line makes a new dictionary containing the extracted weather data, then is returned by the method"""
            "temp_kelvin": temp_kelvin,
            "feels_like_kelvin": feels_like_kelvin,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "description": description,
            "sunrise_time": sunrise_time,
            "sunset_time": sunset_time,
        }


def main():
    """This function runs the program"""
    api_key = "INSERT_API"  # Replace with your actual API key
    city = "INSERT_CITY"
    state = "INSERT_STATE"

    weather = WeatherData(api_key, city, state)
    data = weather.get_weather()

    # celsius, fahrenheit = weather.convert_kelvin_to_celsius_fahrenheit(
    #     data["temp_kelvin"]
    # )

    print(f'Sun rises in {city}, {state} at {data["sunrise_time"]}) local time.')
    print(f'Sun sets in {city}, {state} at {data["sunset_time"]}) local time.')
    print(f'Wind speed in {city}, {state}: {data["wind_speed"]} m/s')
    # You can add similar print statements for other data points


main()
