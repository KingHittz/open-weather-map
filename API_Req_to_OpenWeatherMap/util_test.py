"""this is used to test imports from util_test.py"""

from util import convert_kelvin_to_celsius_fahrenheit

from util import convert_meter_to_mps

from util import convert_kpa_to_psi

from util import convert_inches_to_foot

from util import convert_kpa_to_bar

from util import convert_kpa_to_mmhg

from util import convert_mph_to_kph

from util import convert_degrees_to_cardinal

from util import convert_utc_to_cst


def test_convert_kelvin_to_celsius_fahrenheit():
    """used to test my function from util.py"""

    output = convert_kelvin_to_celsius_fahrenheit(100)
    answer = (-173.14999999999998, -279.66999999999996)
    assert output == answer


def test_convert_meter_to_mps():
    """used to test my function from util.py"""

    output = convert_meter_to_mps(100)
    answer = 223.69400000000002
    assert output == answer


def test_convert_kpa_to_psi():
    """used to test my function from util.py"""
    output = convert_kpa_to_psi(100)
    answer = 14.5038
    assert output == answer


def test_convert_inches_to_foot():
    """used to test my function from util.py"""
    output = convert_inches_to_foot(100)
    answer = 1200.000480000192
    assert output == answer


def test_convert_kpa_to_bar():
    """used to test my function from util.py"""
    output = convert_kpa_to_bar(100)
    answer = 10000.0
    assert output == answer


def test_convert_kpa_to_mmhg():
    """used to test my function from util.py"""
    output = convert_kpa_to_mmhg(100)
    answer = 750.062
    assert output == answer


def test_convert_mph_to_kph():
    """used to test my function from util.py"""
    output = convert_mph_to_kph(100)
    answer = 359.9997120002304
    assert output == answer


def test_convert_degrees_to_cardinal():
    """used to test my function from util.py"""
    output = convert_degrees_to_cardinal(190)
    answer = "S"
    assert output == answer


def test_convert_utc_to_cst():
    """used to test my function from util.py"""
    assert convert_utc_to_cst("2024-06-24 18:00:00") == "2024-06-24 12:00:00"
    assert convert_utc_to_cst("2024-12-25 00:00:00") == "2024-12-24 18:00:00"
    assert convert_utc_to_cst("2024-01-01 06:00:00") == "2024-01-01 00:00:00"
