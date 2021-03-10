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
                
    def combination(self):
    	# Search for combination and score it.
    	self.combination = ""
    	self.score = 0
    	
    	# Check four of a kind.
    	for card in range(2, 15):
    		if self.dictionary['numbers'].count(card) == 4:
    			self.combination = "Four of a Kind"
    			self.score = 105 + four

    	# Check full house and three of a kind.
    	for card in range(2, 15):
    		if self.dictionary['numbers'].count(card) == 3:
    			self.combination = "Three of a Kind"
    			self.score = 45 + card

    	# Check pair and two pairs.
    	pairs = []
    	for card in range(2, 15):
    		if self.dictionary['numbers'].count(card) == 2:
    			pairs.append(card)
    		if len(pairs) == 1:
    			self.combination = "Pair"
    			self.score = 15 + pairs[0]
    		elif len(pairs) == 2:
    			self.combination = "Two Pairs"
    			self.score = 30+ max(pairs) + min(pairs)

    	# Check full house.

    	return self.combination, self.score
        
    def compare_with(self, other):
        pass

string = "2S KS KS AH AS"

me = PokerHand(string)
print(me.combination())

test = {'card1': [13, 'S'], 'card2': [2, 'S'], 'card3': [5, 'S'], 'card4': [11, 'S'], 'card5': [10, 'S']}
list1 = [2, 3, 4, 4, 5]
print(list1.count(4))

