class CardWidget(QtWidgets.QWidget):
    def __init__(self,parent):  
        self.cardSuit = ""
        self.cardNumber = ""
        self.cardBack = QPixmap("CardImgs/back2.jpg")
        self.cardLabel = QtWidgets.QLabel(cardBack)
        self.cardLabel.setPixmap()

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
                self.cardLabel.setPixmap(self.spadesImgs[cardNumIndex])
            elif self.cardSuit == "Hearts":
                self.cardLabel.setPixmap(self.heartsImgs[cardNumIndex])
            elif self.cardSuit == "Clubs":
                self.cardLabel.setPixmap(self.clubsImgs[cardNumIndex])
            else: #self.cardSuit == "Diamonds":
                self.cardLabel.setPixmap(self.diamondsImgs[cardNumIndex])                                                
        else:   #show card back
            self.cardLabel.setPixmap("cardBack.jpg")