from typing import Callable

def calculate(input: str) -> str:
    return str(eval(input))

def planet_mass(planet: str) -> str:
    masses = {
        "Earth": 5.972,
        "Mars": 6.4171,
        "Jupiter": 1.898,
        "Saturn": 5.688,
        "Uranus": 8.686,
        "Neptune": 1.024,
    }
    mass = masses.get(planet, None)
    if mass is None:
        return f"Unknown planet: {planet}"
    return f"{planet} has a mass of {mass} x 10^24 kg"

known_skills: dict[str, Callable[[str], str]] = {
    "calculate": calculate,
    "planet_mass": planet_mass
}
    