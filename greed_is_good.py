#  Greed is a dice game played with five six-sided dice. 
#  Your mission, should you choose to accept it, 
# is to score a throw according to these rules. 
# You will always be given an array with five six-sided dice values.
#
#  Rules:
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point

dice = [5, 1, 3, 4, 1]
def score(dice):
	from collections import Counter
	count = Counter(dice)
	total = 0

	ones = count.get(1)
	if ones:
		if ones >= 3:
			total += 1000 
			ones -= 3
			total += 100 * ones
		else:
			total += 100 * ones
	
	twos = count.get(2)
	if twos:
		if twos >= 3:
			total += 200 
			
	threes = count.get(3)
	if threes:
		if threes >= 3:
			total += 300 
			
	fours = count.get(4)
	if fours:
		if fours >= 3:
			total += 400 
		
	fives = count.get(5)
	if fives:
		if fives >= 3:
			total += 500 
			fives -= 3
			total += 50 * fives
		else:
			total += 50 * fives

	sixs = count.get(6)
	if sixs:
		if sixs >= 3:
			total += 600 
	
	return total
	
print(score(dice))