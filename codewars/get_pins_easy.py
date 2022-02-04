from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
	return [''.join(possible_number) for possible_number in product(*(ADJACENTS[int(number)] for number in observed))]

print(get_pins('66'))