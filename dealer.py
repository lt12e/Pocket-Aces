#Dealer class

import random

class BlackJack:
    def __init__(self, nplayers):
        self.numPlayers = nplayers  
        #player1 = Dealer, player2 = dealer, players3-6 = computer        
        self.players = []
        self.dealer = Dealer()
        self.player = Player()
        self.players.append(self.dealer)
        self.players.append(self.player)
        if nplayers > 1:
            for i in range(self.numPlayers-1):
                self.comp = Player()
                self.players.append(self.comp)

        self.dealer.shuffle()
        self.dealer.deal(self.players)

class Dealer:
	'Blackjack Dealer class'

	def __init__(self):
	#Initializes a list for dealer's hand
	#Initializes the deck from PlayingCards class
		self.hand = []
		self.deck = PlayingCards()

	def deal(self, players):
	#Deals cards to all players
		for card in range(2):
			for player in players:
				player.giveCard(self.getCard())
			self.giveCard(self.getCard())

	def getCard(self):
	#Get card from deck
		self.deck.getCard()

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
			card = self.getCard()
			self.giveCard(card)
			temp = self.getValue(card[0])
			if temp == 11 and score > 10:
				score += 1
			else:
				score += temp
		return score

	def getValue(self, number):
		if number == 14:
			return 11
		elif number > 9:
			return 10
		else:
			return number

	def hit(self, player):
		score = 0
		if len(player.hand) == 2:
			score = self.getValue(player.hand[0][0]) + self.getValue(player.hand[1][0])
		card = self.getCard()
		player.giveCard(card)
		temp = self.getValue(card[0])
		if temp == 11 and score > 10:
			score += 1
		else:
			score += temp
		return score


class Player(Dealer):
	'Blackjack Player sub-class'
	def __init__(self):
	#The player is just a derived form of the Dealer
	#The player has a hand, but not their own deck
	#All functions with the hand are inherited
		self.hand = []

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
