"""This is used for running test on set functions"""

from util import convert_kelvin_to_celsius_fahrenheit


def test_convert_kelvin_to_celsius_fahrenheit():
    """This function is designed to convert a
    temperature value from Kelvin to both Celsius and Fahrenheit"""
    output = convert_kelvin_to_celsius_fahrenheit(100)
    answer = (-173.14999999999998, -279.66999999999996)
    assert output == answer
