#!/usr/bin/env python3


import sys


def vlookup(key, from_dict, to_dict):
    return to_dict.get(from_dict.get(key))


def main(argv):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(argv) == 2:
        value = vlookup(argv[1], states, capital_cities)
        if value is not None:
            print(value)
        else:
            print("Unknown state")


if __name__ == '__main__':
    main(sys.argv)
