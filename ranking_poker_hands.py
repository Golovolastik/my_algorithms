# A famous casino is suddenly faced with a sharp decline of their revenues.
# They decide to offer Texas hold'em also online. 
# Can you help them by writing an algorithm that can rank poker hands?

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
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
        self.dictionary = {}
        for x in range(1, 6):
        	self.dictionary["card{}".format(x)] = self.hand[x-1]
        self.hand = self.dictionary
        for card in self.hand:
        	self.hand[card] = [
        						int(self.hand[card][:-1]),
        						self.hand[card][-1]]

        
    def combination(self):
    	combination = ""

    	return self.hand
        
    def compare_with(self, other):
        pass

string = "KS 2H 5C JD TD"
print(string)

me = PokerHand(string)
print(me.combination())

test = "2H"
print(test[0])

test = {"card1": "10S"}
test["card1"] = [int(test["card1"][:-1]), test["card1"][-1]]
print(test["card1"])
print(test)
