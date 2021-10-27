#!/usr/bin/env python3
def read_numbers(numbers_filename):
	with open(numbers_filename, 'r') as file:
		for line in file:
			array = map(lambda x: x.strip(), line.split(sep=','))
	return array


def main():
	numbers_filename = 'numbers.txt'
	try:
		array = read_numbers(numbers_filename)
		for num in array:
			print(num)
	except IOError as e:
		print("I/O error({0}): {1}".format(e.errno, e.strerror))
	except Exception as e:
		print("Unexpected error:", e)


if __name__ == '__main__':
	main()
