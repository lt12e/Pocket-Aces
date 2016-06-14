#PlayingCards class

import random

class PlayingCards:
	'Deck of cards class'
	
	suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
	number = ["2", "3", "4", "5", "6", "7", "8", "9", 
			  "10", "Jack", "Queen", "King", "Ace"]

	def __init__(self):
	#Makes a list for the deck
	#Then initializes the deck using initialize function
		self.deck = []
		self.initialize()

	def __str__(self):
	#Defines string to print out the current deck
	#Removes all extra characters ex. []()',
		after = ""
		formatting = "[]()',"
		for i in self.deck:
			before = str(i)
			for i in range(len(before)):
				if before[i] not in formatting:
					after += before[i]
			after += "\n"
		return after

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
   
if __name__ == '__main__':
	print "Starting deck of cards"
	deck = PlayingCards()
	print deck
	print "Shuffled cards"
	deck.shuffle()
	print deck
	print "Grabbing a few cards"
	for i in range(6):
		print deck.getCard()
