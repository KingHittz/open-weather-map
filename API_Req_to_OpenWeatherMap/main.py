"""Pulls data from open weather map"""

from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()


class WeatherData:
    """This class represents weather data for a specific location."""

    def __init__(self, city_input, state_input):
        """
        This method initializes the WeatherData object.

        Args:
            api_key (str): Your OpenWeatherMap API key (likely stored in an environment variable)
            city_input (str): The city name for which to retrieve weather data
            state_input (str): The state name for the location (currently unused)
        """
        self.city = city_input
        self.state = state_input
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.api_key = os.getenv("API_KEY")

    def get_weather(self):
        """
        This method retrieves weather data for the location stored in the object.

        Returns:
            dict: A dictionary containing the extracted weather data
        """
        url = f"{self.base_url}appid={self.api_key}&q={self.city}"
        response = requests.get(url, timeout=10).json()
        owmdata = {
            "temp_kelvin": response["main"]["temp"],
            "feels_like_kelvin": response["main"]["feels_like"],
            "wind_speed": response["wind"]["speed"],
            "humidity": response["main"]["humidity"],
            "description": response["weather"][0]["description"],
            "sunrise_time": datetime.fromtimestamp(
                response["sys"]["sunrise"] + response["timezone"]
            ),
            "sunset_time": datetime.fromtimestamp(
                response["sys"]["sunset"] + response["timezone"]
            ),
        }
        return owmdata


if __name__ == "__main__":
    CITY_INPUT = "Manchester"
    STATE_INPUT = "Tennessee"
    weather = WeatherData(CITY_INPUT, STATE_INPUT)
    data = weather.get_weather()
    print(f'Sun rises in {CITY_INPUT}, {STATE_INPUT} at {data["sunrise_time"]}')
    print(f'Sun sets in {CITY_INPUT}, {STATE_INPUT} at {data["sunset_time"]}')
    print(f'Wind speed in {CITY_INPUT}, {STATE_INPUT}: {data["wind_speed"]} m/s')
