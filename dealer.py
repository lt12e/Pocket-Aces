#Dealer class

import random

class BlackJack:
    def __init__(self):
        #player1 = Dealer, player2 = dealer, players3-6 = computer        
        self.dealer = Dealer()
        self.player = Player()
        self.dealer.shuffle()
        self.dealer.deal(self.player)

class Dealer:
	'Blackjack Dealer class'

	def __init__(self):
	#Initializes a list for dealer's hand
	#Initializes the deck from PlayingCards class
		self.hand = []
		self.deck = PlayingCards()
		self.score = 0

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

	def deal(self, player):
	#Deals cards to all players
		self.score = 0
		player.score = 0
		for card in range(2):
			player.giveCard(self.deck.getCard())
			self.giveCard(self.deck.getCard())
		player.get_score()

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

	def play(self):
		score = self.getValue(self.hand[0][0]) + self.getValue(self.hand[1][0])
		while score < 17:
			card = self.deck.getCard()
			self.giveCard(card)
			temp = self.getValue(card[0])
			if temp == 11 and score > 10:
				score += 1
			else:
				score += temp
		self.score = score

	def getValue(self, number):
		if number == 14:
			return 11
		elif number > 9:
			return 10
		else:
			return number

	def hit(self, player):
		score = 0
		card = self.deck.getCard()
		player.giveCard(card)
		temp = self.getValue(card[0])
		if temp == 11 and score > 10:
			score += 1
		else:
			score += temp
		player.score += score


class Player(Dealer):
	'Blackjack Player sub-class'
	def __init__(self):
	#The player is just a derived form of the Dealer
	#The player has a hand, but not their own deck
	#All functions with the hand are inherited
		self.hand = []
		self.score = 0

	def get_score(self):
		self.score = self.getValue(self.hand[0][0]) + self.getValue(self.hand[1][0])

class PlayingCards:
	'Deck of cards class'
	
	suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
	number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

	def __init__(self):
	#Makes a list for the deck
	#Then initializes the deck using initialize function
		self.deck = []
		self.initialize()

	def initialize(self):
	#Initializes the deck
	#Deletes the current deck if necessary
	#Creates a new deck and returns it
		for card in self.deck:
			del card
		for i in range(4):
			for k in range(13):
				card = (self.number[k], self.suit[i])
				self.deck.append(card)
		return self.deck

	def shuffle(self):
	#Shuffles the deck seven times and returns the deck
		for i in range(7):
			random.shuffle(self.deck)
		return self.deck

	def getCard(self):
	#Pops a card from the deck and returns the card
		return self.deck.pop()

"""if __name__ == '__main__':
	print "Creating a quick game"
	dealer = Dealer()
	players = Player()
	dealer.shuffle()
	dealer.deal(players)
	print dealer
	print players"""