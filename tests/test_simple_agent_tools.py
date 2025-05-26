import pytest
from simple_agent_tools import planet_mass, calculate

def test_planet_mass_known_planet():
    # Test with a known planet
    assert planet_mass("Mars") == "Mars has a mass of 6.4171e+24"
    assert planet_mass("Earth") == "Earth has a mass of 5.972e+24"

def test_planet_mass_unknown_planet():
    # Test with an unknown planet
    with pytest.raises(ValueError, match="Unknown planet: Pluto"):
        planet_mass("Pluto")
    with pytest.raises(ValueError, match="Unknown planet: Mercury"):
        planet_mass("Mercury")

def test_planet_mass_case_sensitive():
    # Test case sensitivity
    with pytest.raises(ValueError, match="Unknown planet: mars"):
        planet_mass("mars")
    with pytest.raises(ValueError, match="Unknown planet: MARS"):
        planet_mass("MARS")

def test_planet_mass_empty_string():
    # Test with empty string
    with pytest.raises(ValueError, match="Unknown planet: "):
        planet_mass("")

def test_calculate_simple():
    # Test simple addition
    assert calculate("2 + 3") == "5.000000e+00"

def test_calculate_scientific():
    # Test scientific notation
    assert calculate("1.898e24 + 5.688e24") == "7.586000e+24"

def test_calculate_multiple():
    # Test multiple numbers
    assert calculate("1.898e24 + 6.4171e24 + 5.688e24") == "1.400310e+25"
