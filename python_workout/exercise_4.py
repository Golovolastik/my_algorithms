def hex_output():
	result = 0
	hexnum = input("Enter the hex number to convert: ")
	for power, digit in enumerate(reversed(hexnum)):
		result = int(digit, 16) * 16**power
	print(result)

#hex_output()

# Write a program that asks the user for their name and then produces a “name triangle”: 
#the first letter of their name, then the first two letters, then the first three, 
#and so forth, until the entire name is written on the final line.
def name_triangle():
	name = "Alex"
	#name = input("Enter your name: ")
	for idx, letter in enumerate(name):
		print(f'{name[:idx+1]}')

name_triangle()