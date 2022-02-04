bonus = 1500
price = 2

def beeramid(bonus, price):
	num_of_cans = int(bonus / price)
	if num_of_cans <= 0:
		return 0
	num_of_levels = 0
	while True:
		num_of_levels += 1
		cans_needed = num_of_levels**2
		num_of_cans -= cans_needed
		if num_of_cans < 0:
			num_of_levels -= 1
			break	
	return num_of_levels
		
print(beeramid(bonus, price))