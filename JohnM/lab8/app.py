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

letters_list = []
numbers_list = []
punctuation_list = []


def the_letters(number):
    letters = string.ascii_letters
    for i in range(number):
        letters_list.append(random.choice(letters))


def the_numbers(number):
    numbers = string.digits
    for i in range(number):
        numbers_list.append(random.choice(numbers))


def the_punctuation(number):
    punctuation = string.punctuation
    for i in range(number):
        punctuation_list.append(random.choice(punctuation))


def main():
    the_letters(args["number"])
    the_numbers(args["digits"])
    the_punctuation(args["punctuation"])
    pw = (''.join(letters_list) +
          ''.join(numbers_list) +
          ''.join(punctuation_list))
    random_pw = ''.join(random.sample(pw, len(pw)))

    print(f"Password is {random_pw}")


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
