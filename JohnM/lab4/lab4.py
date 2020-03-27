#!/usr/bin/env python3
"""
Input a grade between 0 and 100
convert the grade to a letter grade.
90 - 100 = A
80 - 89 = B
etc
"""

import random


def get_num_grade():
    """ get a number grade from user
    check that it is between 0 and 100
    return integer num_grade """
    num_grade = int(input("\nEnter a number grade between 0 and 100: "))
    if 0 <= num_grade <= 100:
        return int(num_grade)
    else:
        print(f"\nPlease try again.")
        get_num_grade()


def convert_to_letter(value=100):
    if value >= 90:
        return "A"
    elif value >= 80:
        return "B"
    elif value >= 70:
        return "C"
    elif value >= 60:
        return "D"
    else:
        return "F"


def modifier(value=""):
    plus_minus = value % 10
    if value == 100:
        return "+, nice work!"
    elif plus_minus < 3:
        return "-"
    elif plus_minus > 6:
        return "+"
    else:
        return ""


def get_grade(value=100):
    return convert_to_letter(value), modifier(value)


def main():
    while True:
        question = input("Would you like to check a grade, y/n [y]")
        if question == "n":
            quit()
        else:
            num_grade = get_num_grade()
            rand_grade = random.randint(0, 100)
            letter_grade, letter_mod = get_grade(num_grade)
            print(f"Your grade is {letter_grade}{letter_mod}")
            letter_grade, letter_mod = get_grade(rand_grade)
            print(f"Your competitions grade is {letter_grade}{letter_mod}")


if __name__ == "__main__":
    main()
