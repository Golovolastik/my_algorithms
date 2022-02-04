# Fix function:
#def how_many_dalmatians(n):
#  dogs ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
#  respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
#return respond

def how_many_dalmatians(number):
	dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
	respond = dogs[0] if number <= 10 else (dogs[1] if number <= 50 else(dogs[3] if number == 101 else dogs[2]))
	return respond

print(how_many_dalmatians(26))