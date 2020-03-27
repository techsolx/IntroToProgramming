#!/usr/local/env python3
""""
Let's generate emoticons by assembling a randomly choosing
Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
Pick number of emoticons create,
select horizontal or vertical.
"""

import argparse
import random

eyes = [":", ";", "X", "."]
noses = ["-", "~", "<", "{"]
mouths = [")", "(", "O", "|"]


def print_vertical(e, n, m):
    """ parse inputs, split them,
    add newline.  Print them vertically.
    """
    print(f"{e}\n{n}\n{m}\n")


def randomize(e, n, m):
    r_e = random.choice(eyes)
    r_n = random.choice(noses)
    r_m = random.choice(mouths)
    return r_e, r_n, r_m


def main():
    if args["number"]:
        this_many = args["number"]
    else:
        this_many = 1
    if args["eye"]:
        this_eye = args["eye"]
    else:
        this_eye, _, _ = randomize(eyes, noses, mouths)
    if args["nose"]:
        this_nose = args["nose"]
    else:
        _, this_nose, _ = randomize(eyes, noses, mouths)
    if args["mouth"]:
        this_mouth = args["mouth"]
    else:
        _, _, this_mouth = randomize(eyes, noses, mouths)

    for i in range(this_many):
        if args["vertical"]:
            print_vertical(this_eye, this_nose, this_mouth)
        else:
            print(f"{this_eye}{this_nose}{this_mouth}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create emoticons using the command line as input\n \
        make sure to escape characters that would be caught by your\n \
        interpreter for example, use ")" for ) character, etc.'
    )
    parser.add_argument("-e", "--eye", help="Character to use for the eye", type=str)
    parser.add_argument("-n", "--nose", help="Character to use for the nose", type=str)
    parser.add_argument(
        "-m", "--mouth", help="Character to use for the mouth", type=str
    )
    parser.add_argument(
        "-v", "--vertical", help="Output vertical characters.", action="store_true"
    )
    parser.add_argument(
        "-#", "--number", help="Number of emodicons to use for the mouth", type=int,
    )
    args = vars(parser.parse_args())
    main()
