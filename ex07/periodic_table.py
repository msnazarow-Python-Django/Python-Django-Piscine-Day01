#!/usr/bin/env python3
import os.path


class DotDict(dict):
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


def create_periodic_elem(elem_name, temp_array):
	periodic_elem = {}
	for elem in temp_array:
		key, value = map(lambda x: x.strip(), elem.split(':'))
		periodic_elem[key] = value
	periodic_elem['full'] = elem_name
	periodic_elem = DotDict(periodic_elem)
	periodic_elem.number = int(periodic_elem.number)
	periodic_elem.position = int(periodic_elem.position)
	periodic_elem.molar = float(periodic_elem.molar)
	return periodic_elem


def create_periodic_table_html(file_txt, file_html, file_css_name):
	last_number = 0
	row = '<tr>\n'
	html_table = '''
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Periodic Table</title>
		<link rel="stylesheet" href="{0}"> 
	</head>
	<body>
		<table>
%s
		</table>
	</body>
</html>
'''.format(file_css_name)
	for line in file_txt:
		elem_name, elem_string = map(lambda x: x.strip(), line.split('='))
		temp_array = elem_string.split(',')
		periodic_elem = create_periodic_elem(elem_name, temp_array)
		if periodic_elem.position == 0:
			row = '<tr>\n'
		content = generate_element(periodic_elem, last_number)
		row += content
		if periodic_elem.position == 17:
			row += '</tr>\n%s\n'
			html_table = html_table % row
		last_number = int(periodic_elem.position)
	html_table = html_table % ''
	file_html.write(html_table)


def get_elem_class(periodic_elem):
	element_class = ""
	if periodic_elem.number in (1, 6, 7, 8, 15, 16, 34):
		element_class = "gas1"
	elif periodic_elem.number in (5, 14, 32, 33, 51, 52, 84):
		element_class = "metal5"
	elif periodic_elem.number in (13, 31, 49, 50, 82, 83, 81):
		element_class = "metal4"
	elif periodic_elem.number in (113, 115, 117, 118):
		element_class = "rare1"
	elif periodic_elem.position == 0:
		element_class = "metal1"
	elif periodic_elem.position == 1:
		element_class = "metal2"
	elif 2 <= periodic_elem.position <= 11:
		element_class = "metal3"
	elif periodic_elem.position == 16:
		element_class = "gas2"
	elif periodic_elem.position == 17:
		element_class = "gas3"
	elif periodic_elem.number in (114, 116):
		element_class = "rare2"
	return element_class


def generate_element(periodic_elem, last_number):
	fake_elem = ''
	properties = '''
	<ul>
		<li>
			{:s}
		</li>
		<li>
			{:d}
		</li>
		<li>
			{:.2f}
		</li>
	</ul>
	'''
	span_length = int(periodic_elem.position) - last_number
	if span_length > 2:
		fake_elem = f'<td colspan="{span_length - 1}" style="border:0"></td>\n'
	elif span_length > 1:
		if periodic_elem.number == 72:
			fake_elem = generate_element(
				DotDict({'position': 2, 'number': 71, 'small': 'Lu', 'full': 'Lutetium', 'molar': 174.9668}),
				last_number)
		elif periodic_elem.number == 104:
			fake_elem = generate_element(
				DotDict({'position': 2, 'number': 103, 'small': 'Lr', 'full': 'Lawrencium', 'molar': 262}), last_number)
	element_class = get_elem_class(periodic_elem)
	elem = fake_elem + f'<td class="{element_class}">%s</td>\n'
	args = periodic_elem.small, periodic_elem.number, periodic_elem.molar
	content = properties.format(*args)
	content += f'<h4>{periodic_elem.full}</h4>'
	return elem % content


def generate_css(file_css):
	css = '''
*{
	margin: 0px;
	padding: 0;
	width: 80px;
	align-content: end;
	border-collapse: collapse;
}
td {
	border: 1px solid #000000;
}
ul{
	margin: 1px;
	list-style: none;
	font-size: small;
	position: relative;
}
h4{
	font: 0.8em normal;
}
li:nth-child(1){
	position:relative;
	top: 7px;
	font-size: 2.5em;
	margin-bottom: 0.1em;
}
li:nth-child(2) {
	position: absolute;
	top: -5px;
	text-align: right;
	font-size: 2em;
}
li:nth-child(3) {
	position: absolute;
	top: 0;
	font: 0.9em;
}
.gas1 {
	background-color: cornflowerblue;
}
.gas2 {
	background-color: plum;
}
.gas3 {
	background-color: darkturquoise;
}
.metal1 {
	background-color: burlywood;
}
.metal2 {
	background-color: wheat;
}
.metal3 {
	background-color: darkkhaki;
}
.metal4 {
	background-color: bisque;
}
.metal5 {
	background-color: lightgreen;
}
.rare1 {
	background-color: red;
}
.rare2 {
	background-color: gray;
}
'''
	file_css.write(css)


def main():
	filename = 'periodic_table.txt'
	basename = os.path.splitext(filename)[0]
	try:
		with open(filename, 'r') as file_txt, \
				open(f"{basename}.html", 'w') as file_html, \
				open(f"{basename}.css", 'w') as file_css:
			generate_css(file_css)
			create_periodic_table_html(file_txt, file_html, f"{basename}.css")
	except IOError as e:
		print("I/O error({0}): {1}".format(e.errno, e.strerror))
	except Exception as e:
		print("Unexpected error:", e)


if __name__ == '__main__':
	main()
