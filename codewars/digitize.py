#Given a non-negative integer, return an array / a list of the individual digits in order.
#Examples:
#123 => [1,2,3]
#1 => [1]
#8675309 => [8,6,7,5,3,0,9]

def digitize(n):
	result = []
	for i, j in enumerate(str(n)):
		result.append(int(j))
	return result

print(digitize(8675309))