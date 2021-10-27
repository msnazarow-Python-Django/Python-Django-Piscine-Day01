#!/usr/bin/env python3
import sys


def vlookup(value, from_dict, to_dict):
    return to_dict.get(from_dict.get(value))


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
    capital_cities_reversed = dict(zip(capital_cities.values(), capital_cities.keys()))
    states_reversed = dict(zip(states.values(), states.keys()))
    if len(argv) == 2:
        array = argv[1].split(',')
        for elem in array:
            elem = " ".join(elem.split())
            capital = vlookup(elem.title(), states, capital_cities)
            state = vlookup(elem.title(), capital_cities_reversed, states_reversed)
            if capital is not None:
                print(f'{capital} is the capital city of {elem.title()}')
            elif state is not None:
                print(f'{elem.title()} is the capital city of {state}')
            else:
                print(f'{elem} is neither a capital city nor a state')


if __name__ == '__main__':
    main(sys.argv)

