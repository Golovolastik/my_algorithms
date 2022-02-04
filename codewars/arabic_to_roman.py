number = 1999

def convert(number):
	result = ''
	arabic = [1000, 900, 500, 
	          400, 100, 90, 50,
	          40, 10, 9, 5, 4, 1]
	roman = "M CM D CD C XC L XL X IX V IV I".split()
	table = zip(arabic, roman)
	for arabic, roman in table:
		result += number // arabic * roman
		number %= arabic
	return result
print(convert(number))