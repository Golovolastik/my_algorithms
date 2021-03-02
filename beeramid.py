bonus = 21
price = 1.5

def beeramid(bonus, price):
	num_of_cans = int(bonus / price)
	num_of_levels = 0
	if num_of_cans > 0:
		pass
	else:
		return num_of_levels
	while num_of_cans > 0:
		num_of_levels += 1
		cans_needed = num_of_levels**2
		num_of_cans -= cans_needed
		#print(num_of_cans)
		if num_of_cans <= 0:
			num_of_levels -= 1
			break
	return num_of_levels
		
print(beeramid(bonus, price))