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
    capital_cities = dict(zip(capital_cities.values(), capital_cities.keys()))
    states = dict(zip(states.values(), states.keys()))
    if len(argv) == 2:
        value = vlookup(argv[1], capital_cities, states)
        if value is not None:
            print(value)
        else:
            print("Unknown state")


if __name__ == '__main__':
    main(sys.argv)