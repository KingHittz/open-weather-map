def convert_kelvin_to_celsius_fahrenheit(kelvin):
    """This function is designed to convert a temperature value from Kelvin to both Celsius and Fahrenheit"""
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit
