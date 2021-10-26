def read_numbers(numbers_filename):
    with open(numbers_filename, 'r') as file:
        for line in file:
            array = line.strip('\n').split(sep=',')
    return array


def main():
    numbers_filename = 'numbers.txt'
    array = read_numbers(numbers_filename)
    for num in array:
        print(num)


if __name__ == '__main__':
    main()
