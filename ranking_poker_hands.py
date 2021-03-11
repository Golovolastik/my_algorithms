# A famous casino is suddenly faced with a sharp decline of their revenues.
# They decide to offer Texas hold'em also online. 
# Can you help them by writing an algorithm that can rank poker hands?

class PokerHand(object):

    #RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
    	# Hand preprocessing
        self.hand = hand.split(" ")
        for pos, card in enumerate(self.hand):
        	if card[0] == "T":
        		self.hand[pos] = card.replace("T", "10")
        	elif card[0] == "J":
        		self.hand[pos] = card.replace("J", "11")
        	elif card[0] == "Q":
        		self.hand[pos] = card.replace("Q", "12")
        	elif card[0] == "K":
        		self.hand[pos] = card.replace("K", "13")
        	elif card[0] == "A":
        		self.hand[pos] = card.replace("A", "14")
        
        # Creating dictionary.
        self.dictionary = {}
        self.suit_list = []
        self.number_list = []
        for idx in range(5):
        	self.suit_list.append(self.hand[idx][-1])
        	self.number_list.append(int(self.hand[idx][:-1]))
        self.dictionary['suit'] = self.suit_list
        self.dictionary['numbers'] = self.number_list
        # Count repetitions of numbers in the hand.
        self.rnum = [self.dictionary['numbers'].count(i) for i in self.dictionary['numbers']]
        # Count repetitions of suits in the hand.
        self.rsuits = [self.dictionary['suit'].count(i) for i in self.dictionary['suit']]
        # The difference between the greater and the smallest number in the hand.
        self.dif = max(self.dictionary['numbers']) - min(self.dictionary['numbers']) 
                
    def combination(self):
    	# Search for combination and score it.
    	self.combination = ""
    	self.score = 0
    	# Additional variables which helps to score some combinations.
    	self.temp_score1 = 0
    	self.temp_score2 = 0

    	# Start checking from the best combinations.
    	# Check for a royal and street flush, and flush itself.
    	if 5 in self.rsuits:
    		if sorted(self.dictionary['numbers']) == [10, 11, 12, 13, 14]:
    			self.combination = "Royal Flush"
    			self.score = 1
    			return self.combination, self.score
    		elif self.dif == 4 and max(self.rnum) == 1:
    			self.combination = "Street Flush"
    			self.score = 15 - max(self.dictionary['numbers'])  # max score - 9
    			return self.combination, self.score
    		else:
    			self.combination = "Flush"
    			self.temp_score1 = (15 - sorted(self.dictionary['numbers'])[-1]) + \
    							   (15 - sorted(self.dictionary['numbers'])[-2]) / 100 + \
    							   (15 - sorted(self.dictionary['numbers'])[-3]) / 1_000 + \
    							   (15 - sorted(self.dictionary['numbers'])[-4]) / 10_000 + \
    							   (15 - sorted(self.dictionary['numbers'])[-5]) / 100_000
    			self.score = 35 + self.temp_score1  # max score - 44.*****
    			return self.combination, self.score

    	# Check four of a kind.
    	if 4 in self.rnum:
    		self.combination = "Four of a Kind"
    		for card in self.dictionary['numbers']:
    			if self.dictionary['numbers'].count(card) == 4:
    				self.score = 24 - card  # max score - 22
    				break
    		return self.combination, self.score

    	# Check full house.
    	if sorted(self.rnum) == [2, 2, 3, 3, 3]:
    		self.combination = "Full House"
    		for card in self.dictionary['numbers']:
    			if self.dictionary['numbers'].count(card) == 3:
    				self.temp_score1 = 15 - card
    			else:
    				self.temp_score2 = (15 - card) / 100
    				break
    		self.score = 22 + self.temp_score1 + self.temp_score2 # max score - 35.**
    		return self.combination, self.score

    	# Check straight.
    	if self.dif == 4 and max(self.rnum) == 1:
    		self.combination = "Straight"
    		self.score = 59 - max(self.dictionary['numbers']) # max score - 53
    		return self.combination, self.score

    	# Check three of a kind.
    	if 3 in self.rnum:
    		self.combination = "Three of a Kind"
    		for card in self.dictionary['numbers']:
    			if self.dictionary['numbers'].count(card) == 3:
    				self.temp_score1 = 15 - card
    				break 
    		self.score = 53 + self.temp_score1 # max score - 66
    		return self.combination, self.score 

    	# Check pair and two pairs.
    	pairs = []
    	for card in range(2, 15):
    		if self.dictionary['numbers'].count(card) == 2:
    			pairs.append(card)
    		if len(pairs) == 1:
    			self.combination = "Pair"
    			self.temp_score1 = 15 - pairs[0]
    			self.score = 78 + self.temp_score1
    			return self.combination, self.score
    		elif len(pairs) == 2:
    			self.combination = "Two Pairs"
    			self.temp_score1 = 15 - max(pairs)
    			self.temp_score2 = (15 - min(pairs)) / 100
    			self.score = 66 + self.temp_score1 + self.temp_score2 # max score - 78.**
    			return self.combination, self.score

    	return f"You have {self.combination}, and have {self.score} score.", self.rsuits, self.rnum

    def compare_with(self, other):
        pass

string = "2H 2S 4S 3H 6H"

me = PokerHand(string)
print(me.combination())

test = {'card1': [13, 'S'], 'card2': [2, 'S'], 'card3': [5, 'S'], 'card4': [11, 'S'], 'card5': [10, 'S']}
list1 = [2, 3, 4, 4, 5]
print(list1.count(4))

