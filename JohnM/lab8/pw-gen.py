#!/usr/bin/env python3
"""
Lab 8: Password Generator
Let's generate a password ten characters long using a loop (`while` loop or
`for` loop) and `random.choice`, this will be a string of random characters.
## Advanced Version 1
Allow the user to choose how many characters the password will be.
## Advanced Version 2
Allow the user to choose how many letters, numbers, and punctuation
characters they want in their password. Mix everything up using `list()`,
`random.shuffle()`, and `''.join()`.
"""

import argparse
import random
import string

letters = string.ascii_letters


letters = []
numbers = []
puncutation = []


def the_letters(number):
    letters = random.choice(string.ascii_letters)
    for i in range(number):
        letters.append(random.choice(letters))
    return letters


def the_numbers(number):
    numbers = random.choise(string.digtits)
    for i in range(number):
        numbers.append(random.choice(numbers))
    return numbers


def the_punctuation(number):
    punctuation = random.choise(string.punctuation)
    for i in range(number):
        punctuation.append(random.choice(punctuation))
    return punctuation


def main():
    the_letters(args["number"])
    the_numbers(args["digits"])
    the_punctuation(args["punctuation"])
    pw = ''.join(l) + ''.join(ddn + p
    print(f"Password is {random.shuffle(pw)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate a password using a series of characters\n \
        select if you want to add numbers, or punctuation characters'
    )
    parser.add_argument(
        "-n", "--number",
        help="Number of characters to use",
        type=int,
        default=10
    )
    parser.add_argument(
        "-d", "--digits",
        help="Number of digits to inclued",
        type=int,
        default=0,
    )
    parser.add_argument(
        "-p", "--punctuation",
        help="Number of punctuation characters to inclued",
        type=int,
        default=0,
    )
    args = vars(parser.parse_args())
    main()
