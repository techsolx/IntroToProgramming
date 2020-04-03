#!/usr/bin/env python3
"""
convert between units
feet, miles, meters and kilometers
"""
import json


distance = int(input(f"What is the distance? "))
i_units = input(f"What are the input units, [ft,mi,m,km]? ")
o_units = input(f"What are the output units [ft,mi,m,km]? ")
dist_dict = {"ft2m": 0.3048}
key = i_units + '2' + o_units


def dump_json():
    with open("dist-dict.json", "w") as f:
        json.dump(dist_dict, f)


def get_json():
    with open("dist-dict.json", "r") as f:
        json.load(dist_dict, f)


def add_conversion(i_units, o_units, key):
    print(f"I don't have the conversion {i_units} to {o_units} in my table.")
    conversion = float(input(f"How many {i_units} to an {o_units}? "))
    dist_dict[key] = conversion
    dump_json()


def try_again():
    question = input(
        f"Would you like to convert another value? y/n [y] "
    )
    if question == "n":
        dump_json()
        quit()
    else:
        return True


def convert(key):
    converted_val = dist_dict[key] * distance
    print(f"{distance}{i_units} is {converted_val:.4f}{o_units}")


def main():
    while True:
        if key in dist_dict:
            convert(key)
            try_again()
        else:
            add_conversion(i_units, o_units, key)
            convert(key)
            try_again()



if __name__ == "__main__":
    main()
