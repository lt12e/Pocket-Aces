class CardWidget(QtWidgets.QWidget):
    def __init__(self,parent):  
        self.cardSuit = ""
        self.cardNumber = ""
        self.cardBack = QImage()
        self.cardBack.load("CardImgs/back2.jpg")
        self.cardLabel = QtWidgets.QLabel()
        self.cardLabel.setPixmap(self.cardBack)
        self.spadesImgs = ['2_of_spades.png', '3_of_spades.png', '4_of_spades.png', '5_of_spades.png', '6_of_spades.png', '7_of_spades.png', '8_of_spades.png', '9_of_spades.png', '10_of_spades.png', "jack_of_spades2", "queen_of_spades2", "king_of_spades2", "ace_of_spades2"]
        self.heartsImgs = ['2_of_hearts.png', '3_of_hearts.png', '4_of_hearts.png', '5_of_hearts.png', '6_of_hearts.png', '7_of_hearts.png', '8_of_hearts.png', '9_of_hearts.png', '10_of_hearts.png', "jack_of_hearts2", "queen_of_hearts2", "king_of_hearts2", "ace_of_hearts2"]
        self.clubsImgs = ['2_of_clubs.png', '3_of_clubs.png', '4_of_clubs.png', '5_of_clubs.png', '6_of_clubs.png', '7_of_clubs.png', '8_of_clubs.png', '9_of_clubs.png', '10_of_clubs.png', "jack_of_clubs2", "queen_of_clubs2", "king_of_clubs2", "ace_of_clubs2"]
        self.diamondsImgs = ['2_of_diamonds.png', '3_of_diamonds.png', '4_of_diamondsades.png', '5_of_diamonds.png', '6_of_diamonds.png', '7_of_diamonds.png', '8_of_diamonds.png', '9_of_diamonds.png', '10_of_diamonds.png', "jack_of_diamonds2", "queen_of_diamonds2", "king_of_diamonds2", "ace_of_diamonds2"]

    def setCard(c): #c = a card tuple
        self.cardSuit = c[1] #2nd value in card tuple
        self.cardNumber = c[0] #1st value in card tuple

    def showFront(self,b):
        if b == True:   #show front of card
            #TODO get cardNumIndex from gameObj?
            self.cardNumIndex = -1
            if self.cardNumber == "Ace":
                self.cardNumIndex == 12
            elif self.cardNumber == "King":
                self.cardNumIndex == 11
            elif self.cardNumber == "Queen":
                self.cardNumIndex == 10
            elif self.cardNumber == "Jack":
                self.cardNumIndex == 9
            else:
                self.cardNumIndex == int(self.cardNumber)

            if self.cardSuit == "Spades":
                self.cardLabel.setPixmap("CardImgs/" + self.spadesImgs[cardNumIndex])
            elif self.cardSuit == "Hearts":
                self.cardLabel.setPixmap("CardImgs/" + self.heartsImgs[cardNumIndex])
            elif self.cardSuit == "Clubs":
                self.cardLabel.setPixmap("CardImgs/" + self.clubsImgs[cardNumIndex])
            else: #self.cardSuit == "Diamonds":
                self.cardLabel.setPixmap("CardImgs/" + self.diamondsImgs[cardNumIndex])                                                
        else:   #show card back
            self.cardLabel.setPixmap("cardBack.jpg")