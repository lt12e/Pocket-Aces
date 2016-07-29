#Dealer class

from PlayingCards import PlayingCards

class Dealer:
	'Poker Dealer class'

	def __init__(self):
	#Initializes a list for dealer's hand
	#Initializes the deck from PlayingCards class
		self.hand = []
		self.deck = PlayingCards()
		self.name = ""
		self.money = 2000

	def __str__(self):
	#Defines print to print out the current HAND
	#Removes extra characters ex. []()',
		after = ""
		formatting = "[]()',"
		for i in self.hand:
			before = str(i)
			for i in range(len(before)):
				if before[i] not in formatting:
					after += before[i]
			after += "\n"
		return after

	def deal(self, players, game="five"):
	#Deals cards to all players
	#Defaulted to five cards each for five card draw
	#game can be set to "texas" for two cards each
		if game == "texas":
			for card in range(2):
				for player in players:
					player.giveCard(self.deck.getCard())
				self.giveCard(self.deck.getCard())
		elif game == "five":
			for card in range(5):
				for player in players:
					player.giveCard(self.deck.getCard())
				self.giveCard(self.deck.getCard())

	def giveCard(self, card):
	#Takes card from deck and gives to hand
		self.hand.append(card)

	def emptyHand(self):
	#Empties the current hand of cards
		for card in self.hand:
			del card

	def shuffle(self):
	#Re-initializes the deck to full
	#Shuffles deck to ready for next deal
		self.deck.initialize()
		self.deck.shuffle()

	def swap(self, player, card1, card2=0, card3=0):
	#Allows player to swap up to three cards for new ones
	#Removes each card from players hand
	#Appends new card after removal
		hand = player.hand
		one = hand[card1]
		if card2:
			two = hand[card2]
			if card3:
				hand.remove(hand[card3])
				hand.append(self.deck.getCard())
			hand.remove(two)
			hand.append(self.deck.getCard())
		hand.remove(one)
		hand.append(self.deck.getCard())
		return hand

	def setName(self,n):
		#Sets the Dealer's name
		self.name = n

	def getName(self):
		return self.name

	def setMoney(self, m):
		self.money = m

	def getMoney(self):
		return self.money

class Player(Dealer):
	'Poker Player sub-class'
	def __init__(self):
	#The player is just a derived form of the Dealer
	#The player has a hand, but not their own deck
	#All functions with the hand are inherited
		self.hand = []

if __name__ == '__main__':
	print "Creating a quick game"
	dealer = Dealer()
	players = [Player(), Player(), Player(), Player()]
	dealer.shuffle()
	dealer.deal(players)
	print dealer
	for player in players:
		print player
	dealer.swap(players[3], 0, 1, 2)
	print "swapped"
	print players[3]
