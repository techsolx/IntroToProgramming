#!/usr/bin/env python3
"""
lab-02 for PDX Code Guild 101 course.
Create mad lib game for a phrase or lyric
"""

noun = input("Give me a noun? ")
verb = input("Give me a verb? ")
adjective = input("Give me a adjective? ")
diety = input("Give me a diety? ")
vehicle = input("Give me a vehicle? ")

adjectives = []


def get_adj():
    """
    get a list of 3 adjectives
    loop through them to return one.
    """
    pass


print(
    f"\n\n"
    f"Well, I don't care if it rains or {adjective},\n"
    f"Long as I have my plastic {diety}\n"
    f"Riding on the dashboard of my {vehicle}\n"
    f"Through all trials and tribulations,\n"
    f"We will travel every nation,\n"
    f"With my plastic {diety} I'll go far.\n"
)
