#!/usr/bin/env python3
"""
lab-01 for PDX Code Guild 101 course.
successfully install python3,
create and run a simple hello world program.
"""
major_planets = [
    "MERCURY",
    "VENUS",
    "EARTH",
    "MARS",
    "JUPITER",
    "SATURN",
    "URANUS",
    "NEPTUNE",
]
minor_planets = [
    "CERES",
    "PLUTO",
    "ERIS",
    "SEDNA",
]


def upper_first_letter(s):
    return s[0].upper() + s[1:]


while True:
    input_planet = input("Type in the name of a planet, or type quit() to exit? ")
    if input_planet == "quit()":
        quit()
    if input_planet.upper() in major_planets:
        input_planet_case = upper_first_letter(input_planet)
        print(f"You picked a Major Planet, I will say Hello {input_planet_case}")
    elif input_planet.upper() in minor_planets:
        input_planet_case = upper_first_letter(input_planet)
        print(f"You picked a Minor Planet, I will say Hello {input_planet_case}")
    else:
        input_planet_case = upper_first_letter(input_planet)
        print(f"I don't know that planet, I will just say Hello {input_planet_case}")
