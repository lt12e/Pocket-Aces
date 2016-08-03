''' BlackJack.py '''

from playingcards import PlayingCards
from dealer import Dealer, Player

class BlackJack:
    def __init__(self, nplayers):
        self.numPlayers = nplayers  
        #player1 = Dealer, player2 = dealer, players3-6 = computer        
        self.players = []
        self.dealer = Dealer()
        self.player = Player()
        self.players.append(self.dealer)
        self.players.append(self.player)
        for i in range(self.numPlayers-1):
            self.comp = Player()
            self.players.append(self.comp)

        #set player names
        self.players[0].name = "Dealer"
        self.players[1].name = "You" #can be changed
        for i in range(len(self.players)-2):
            self.players[i+2].name = "Player " + str(i+1)
        self.dealer.shuffle()
        self.Deal()

    def PlayGame(self):
        cont = True
        while cont:
            #TODO finish this
            cont = False


    def Deal(self):
        self.dealer.deal(self.players, "blackjack")

    def Hit(self, player): 
        #Give the player a card from the deck
        pass

    #Stand option can be handled by the GUI

    def TakeInsurance(self, player):
        pass

    def DoubleDown(self, player):
        #double the bet and get only one more card (the hold on the card will be handled by game_frame.py)
        pass

    def Split(self, player):
        #Dealer/Player class was edited to have up to two hands for this
        pass

    def FindWinner(self):
        self.scores = []
        self.winnerTuple = None
        for p in self.players:
            self.scores.append(p.name, ScoreHand(p.hand))
            if p.hand2 != []:
                self.scores.append(p.name, ScoreHand(p.hand2))

        #TODO deal with ties here
        #TODO set winnerTuple with the winner and the score
        return self.winnerTuple

    def ScoreHand(self, hand): #hand is a list of cards, a card is a tuple of format (suit, number)
        self.total = 0
        self.aces = 0
        for x in hand:
            if x[1] == "Ace":
                aces += 1
            elif x[1] == "10" or x[1] == "Jack" or x[1] == "Queen" or x[1] == "King":
                total += 10
            else:
                total += int(x[1])

        if self.aces > 0:
            #TODO try to add aces to score so that the score is as close to 21 without going over
            pass

        return self.total



    #Surrender option can be added but IS NOT NECESSARY