#  Sheldon, Leonard, Penny, Rajesh and Howard are in the queue 
# for a "Double Cola" drink vending machine; 
# there are no other people in the queue. 
# The first one in the queue (Sheldon) buys a can, drinks it and doubles!
# The resulting two Sheldons go to the end of the queue.
# Then the next in the queue (Leonard) buys a can, 
# drinks it and gets to the end of the queue as two Leonards, and so on.

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

def who_is_next(names, r):
	if r <= len(names):
		return names[r-1]
	temp = len(names)
	power = 1
	while temp:
		if (temp + 2**power * len(names)) >= r:
			for i in range(len(names)):
				temp += 2**power
				if temp >= r:
					return names[i]
		else:
			power += 1
			temp += 2**(power - 1) * len(names)

print(who_is_next(names, 23)) 
