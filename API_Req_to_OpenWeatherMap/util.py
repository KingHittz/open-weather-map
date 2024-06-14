"""unused utilities will be stored here"""


def convert_kelvin_to_celsius_fahrenheit(kelvin):
    """This function is designed to convert a
    temperature value from Kelvin to both Celsius and Fahrenheit"""
    celsius: kelvin = kelvin - 273.15
    fahrenheit: celsius = celsius * (9 / 5) + 32
    return celsius, fahrenheit


# celsius, fahrenheit = weather.convert_kelvin_to_celsius_fahrenheit(data["temp_kelvin"])


def convert_speed_to_mps(value, unit_from="m/s"):
    """Converts speed from meters
    per second to miles per hour"""

    conversion_factor = 2.23694

    if unit_from.upper() != "M/S":
        raise ValueError(f"Unsupported unit: {unit_from}")
    return value * conversion_factor


def convert_kpa_to_psi(value):
    """converts kPa to psi"""
    psi = value * 0.145038
    return psi


def convert_inches_to_foot(value):
    """converts inches to foot"""
    foot = value / 0.0833333
    return foot


def convert_kpa_to_bar(value):
    """converts kPa to bar"""
    bars = value / 0.01
    return bars


def convert_kpa_to_mmhg(value):
    """converts kPa to mmhg"""
    mmhg = value * 7.50062
    return mmhg


def convert_mph_to_kph(value):
    """converts mph to kph"""
    kph = value / 0.277778
    return kph


def degrees_to_cardinal(degrees):
    """Converts degrees to cardinal direction"""

    if degrees >= 0 or degrees < 360:
        return "N"

    elif degrees < 90:
        return "E"

    elif degrees < 180:
        return "S"

    elif degrees < 270:
        return "W"

    return degrees









