import pytest
from simple_agent_tools import planet_mass

def test_planet_mass_known_planet():
    # Test with a known planet
    assert planet_mass("Mars") == "Mars has a mass of 6.4171 x 10^24 kg"
    assert planet_mass("Earth") == "Earth has a mass of 5.972 x 10^24 kg"

def test_planet_mass_unknown_planet():
    # Test with an unknown planet
    assert planet_mass("Pluto") == "Unknown planet: Pluto"
    assert planet_mass("Mercury") == "Unknown planet: Mercury"

def test_planet_mass_case_sensitive():
    # Test case sensitivity
    assert planet_mass("mars") == "Unknown planet: mars"
    assert planet_mass("MARS") == "Unknown planet: MARS"

def test_planet_mass_empty_string():
    # Test with empty string
    assert planet_mass("") == "Unknown planet: "
