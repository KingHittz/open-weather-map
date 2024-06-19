from util import convert_kelvin_to_celsius_fahrenheit

from util import convert_speed_to_mps

from util import convert_kpa_to_psi

from util import convert_inches_to_foot

from util import convert_kpa_to_bar

from util import convert_kpa_to_mmhg

from util import convert_mph_to_kph

from util import degrees_to_cardinal

# from util import utc_to_cst

def test_convert_kelvin_to_celsius_fahrenheit():
    output = convert_kelvin_to_celsius_fahrenheit(100)
    answer = (-173.14999999999998, -279.66999999999996)
    assert output == answer


def test_convert_speed_to_mps():
    output = convert_speed_to_mps(100)
    answer = 223.69400000000002
    assert output == answer


def test_convert_kpa_to_psi():
    output = convert_kpa_to_psi(100)
    answer = 14.5038
    assert output == answer


def test_convert_inches_to_foot():
    output = convert_inches_to_foot(100)
    answer = 1200.000480000192
    assert output == answer


def test_convert_kpa_to_bar():
    output = convert_kpa_to_bar(100)
    answer = 10000.0
    assert output == answer


def test_convert_kpa_to_mmhg():
    output = convert_kpa_to_mmhg(100)
    answer = 750.062
    assert output == answer


def test_convert_mph_to_kph():
    output = convert_mph_to_kph(100)
    answer = 359.9997120002304
    assert output == answer


def test_degrees_to_cardinal():
    output = degrees_to_cardinal(90)
    answer = "E"
    assert output == answer

def test_utc_to_cst():
    output = utc_to_cst()
    answer =
    assert output == answer
