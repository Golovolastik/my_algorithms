def pig_latin(str):
	vovel = ('a', 'e', 'i', 'o', 'u')
	if str[0] in vovel:
		return str + 'way'
	else:
		return str[1:] + str[0].lower() + 'ay'

print(pig_latin('Python'))