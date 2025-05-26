from typing import Callable

def calculate(input: str) -> str:
    try:
        result = eval(input)
        if isinstance(result, (int, float)):
            return f"{result:.6e}"
        raise ValueError("Result is not a number")
    except Exception as e:
        return f"Invalid calculation: {input} - {str(e)}"

def planet_mass(planet: str) -> str:
    masses = {
        "Earth": 5.972e24,
        "Mars": 6.4171e24,
        "Jupiter": 1.898e24,
        "Saturn": 5.688e24,
        "Uranus": 8.686e24,
        "Neptune": 1.024e24,
    }
    mass = masses.get(planet, None)
    if mass is None:
        raise ValueError(f"Unknown planet: {planet}")
    
    return f"{planet} has a mass of {mass}"

known_skills = {
    "calculate": calculate,
    "planet_mass": planet_mass
}
    