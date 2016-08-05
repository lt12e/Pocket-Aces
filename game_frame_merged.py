''' game_frame.py '''

## wood.jpg from http://www.textureking.com/content/img/stock/big/DSC_6096.JPG
## redseamless.jpg from http://www.myfreetextures.com/wp-content/uploads/2014/10/seamless-wood3.jpg
## green-gradient.jpg from http://www.technocrazed.com/wp-content/uploads/2015/12/Green-Wallpaper-1.jpg
## jungle-green-grunge-texture.jpg from http://www.texturecrate.com/texture/jungle-green-grunge/
## logo.jpg by Jeffrey Campbell

##back2.jpg from http://www.leeasher.com/store/playing_cards/tally_ho_red.html
## back.png from http://becuo.com/cool-playing-cards-back


import sys#, os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from dealer import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.createStartFrame()

    ## Load Screen ##
    def createStartFrame(self):
        self.setWindowTitle('Pocket-Aces')
        self.mainLayout = Background(self)
        self.setCentralWidget(self.mainLayout)
        self.setStyleSheet("QMainWindow { background: 'black'}");

        ## Menu Options ##
        menuBar = self.menuBar().addMenu('File')
        self.newGameOption = menuBar.addAction('New Game')
        self.newGameOption.triggered.connect(self.mainLayout.newGame)
        self.loadGameOption = menuBar.addAction('Load Game')
        self.loadGameOption.triggered.connect(self.mainLayout.loadGame)
        self.loadGameOption.setVisible(False)
        self.saveGameOption = menuBar.addAction('Save Game')
        self.saveGameOption.triggered.connect(self.mainLayout.saveGame)
        self.saveGameOption.setVisible(False)
        self.changeTableOption = menuBar.addAction('Change Table Style')
        self.changeTableOption.triggered.connect(self.changeTableStyle)
        self.exitGameOption = menuBar.addAction('Exit')
        self.exitGameOption.triggered.connect(QtWidgets.qApp.quit)   #could add popup with save option

        self.show()

    def changeTableStyle(self):
        if self.mainLayout.tStyle == 1:
            self.mainLayout.tStyle = self.mainLayout.changeTableStyle(1)
            self.mainLayout.repaint()
        else:
            self.mainLayout.tStyle = self.mainLayout.changeTableStyle(2)
            self.mainLayout.repaint()

## App Background Layout (level 1) ##
class Background(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.tStyle = 1
        self.numPlayers = 0
        self.setFixedSize(1001,601)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor('black'))
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.bbox = QtWidgets.QHBoxLayout()

        self.setInitLayout()

        self.setLayout(self.hbox)

    def paintEvent(self,event):
        ## Table Setup ##
        qp = QtGui.QPainter()
        qp.begin(self)
        pen = qp.pen()
        pen.setColor(QtGui.QColor(QtCore.Qt.transparent))
        qp.setPen(pen)
        edgeBrush = QtGui.QBrush()
        tableBrush = QtGui.QBrush() #reset brush

        if self.tStyle == 1:
            edgeBrush.setTextureImage(QtGui.QImage('redseamless.jpg'))
            tableBrush.setTextureImage(QtGui.QImage('jungle-green-grunge-texture.jpg'))
        else: #self.tStyle == 2
            edgeBrush.setTextureImage(QtGui.QImage('wood.jpg'))
            tableBrush.setTextureImage(QtGui.QImage('green-gradient.jpg'))

        qp.setBrush(edgeBrush)
        qp.drawEllipse(-150,-650,1300,1300)
        qp.setPen(pen)
        qp.setBrush(tableBrush)
        qp.drawEllipse(-120,-620,1240,1240)

        qp.end()

    def setInitLayout(self):
                ## Inital screen elements ##
        self.logo = QtWidgets.QLabel()
        self.logoPixmap = QtGui.QPixmap("logo.png")
        self.logo.setPixmap(self.logoPixmap)
        self.newButton = QtWidgets.QPushButton('New Game')
        self.newButton.setToolTip('Begin a new game')
        self.newButton.clicked.connect(self.newGame)
        self.newButton.setFixedWidth(80)
        self.loadButton = QtWidgets.QPushButton('Load Game')
        self.loadButton.setToolTip('Load a previous game')
        self.loadButton.clicked.connect(self.loadGame)
        self.loadButton.setFixedWidth(80)
        self.loadButton.setVisible(False)

        ## Game choice screen elements ##
        self.gameModeLabel = QtWidgets.QLabel('Which game will you play?')
        self.gameModeLabel.setStyleSheet("font: bold; color: white; font-size:24px; background-position: center")
        self.gameModeLabel.setVisible(False)
        self.gameModeCombo = QtWidgets.QComboBox()
        self.gameModeCombo.addItems(['BlackJack'])
        # self.gameModeCombo.addItems(['BlackJack','Texas Hold \'Em'])
        self.gameModeCombo.setVisible(False)
        self.playersLabel = QtWidgets.QLabel('How many players (excluding you and the dealer)?')
        self.playersLabel.setStyleSheet("font: bold; color: white; font-size:24px; background-position: center")
        self.playersLabel.setVisible(False)
        self.playersCombo = QtWidgets.QComboBox()
        self.playersCombo.addItems(['1','2','3','4'])
        self.playersCombo.setVisible(False)
        self.playersComboOk = QtWidgets.QPushButton('OK')
        self.playersComboOk.clicked.connect(self.getNumPlayers)
        self.playersComboOk.setVisible(False)
        self.comboBoxLayout = QtWidgets.QHBoxLayout()
        self.comboBoxLayout.addWidget(self.playersCombo)
        self.comboBoxLayout.addWidget(self.playersComboOk)

        ## Place button(s) in the middle of the screen ##
        self.hbox.addStretch(.5)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(.5)

        self.vbox.addStretch(.4)
        self.vbox.addWidget(self.logo)

        self.bbox.addStretch(.5)
        self.bbox.addWidget(self.newButton)
        self.bbox.addWidget(self.loadButton)
        self.bbox.addStretch(.5)
        self.vbox.addStretch(.1)
        self.vbox.addLayout(self.bbox)
        self.vbox.addWidget(self.gameModeLabel)
        self.vbox.addWidget(self.gameModeCombo)
        self.vbox.addWidget(self.playersLabel)
        self.vbox.addLayout(self.comboBoxLayout)        
        self.vbox.addStretch(.4)

    def changeTableStyle(self, tableStyle):
        if tableStyle == 1:
            return 2
        else: #tableStyle == 2
            return 1

    def newGame(self):
        if self.newButton.isVisible():
            self.newButton.setVisible(False)
        else: #currently in a game, reachable by the new game menu option
            pass
            #check with player to save game
            #hide gameplayWidget layout
            #AND/OR set self.hbox as the current layout (central widget?)
        self.preGameInfoSetVisible(True)



    def loadGame(self):
        print("background.loadGame triggered")
    #     #open loadPopup

    def saveGame(self):
        print("background.saveGame triggered")

    def getNumPlayers(self):
        self.numPlayers = self.playersCombo.currentIndex() + 1
        self.gameMode = self.gameModeCombo.currentIndex() + 1

        self.preGameInfoSetVisible(False)
        if self.hbox.isEnabled():
            self.hbox.setEnabled(False)

        self.initGame()
       

    def preGameInfoSetVisible(self,b):
        self.gameModeLabel.setVisible(b)
        self.gameModeCombo.setVisible(b)
        self.playersLabel.setVisible(b)
        self.playersCombo.setVisible(b)
        self.playersComboOk.setVisible(b)
        self.logo.setVisible(b)

    def initGame(self):
        # self.parent.parent.saveGameOption.setVisible(True) #activate save game option in file menu
        self.gameObj = None
        if self.gameMode == 1:
            self.gameObj = BlackJack()  
            self.initGameplayWidget()
        else: #gameMode == 2
            self.gameObj = TexasHoldEm()
            gameObj.setNumPlayers(self.numPlayers+2) 
            self.initGameplayWidget()

    def hit_game(self):
        if self.gameObj.player.score > 21:
            pass
        else:
            self.gameObj.dealer.hit(self.gameObj.player)
            self.newCardNum = self.gameObj.player.hand[self.count]
            self.newCardFace = self.findFace(self.newCardNum)
            self.newCardPix = QtGui.QPixmap(self.newCardFace)
            if self.count == 2:
                self.playerCard3.setPixmap(self.newCardPix)
            if self.count == 3:
                self.playerCard4.setPixmap(self.newCardPix)
            if self.count == 4:
                self.playerCard5.setPixmap(self.newCardPix)
            if self.count == 5:
                self.playerCard6.setPixmap(self.newCardPix)
            if self.count == 6:
                self.playerCard7.setPixmap(self.newCardPix)
            if self.count == 7:
                self.playerCard8.setPixmap(self.newCardPix)
            if self.count == 8:
                self.playerCard9.setPixmap(self.newCardPix)
            if self.count == 9:
                self.playerCard10.setPixmap(self.newCardPix) 
            if self.count == 10:
                self.playerCard11.setPixmap(self.newCardPix)                                


            if self.gameObj.player.score > 21:
                self.message.setText("Player has Bust! You Lose!")
            if self.gameObj.player.score == 21:
                self.message.setText("Player hits 21! You Win!")
            else:
                self.count += 1

    def deal_cards(self):

        self.gameObj.dealer.shuffle()
        self.gameObj.dealer.deal(self.gameObj.player)
        self.set_cards()
        self.count = 2
        # del self.gameObj.player.aces[:]

    def player_stands(self):
# print "player stands"
#         print "player final score",
#         print self.gameObj.player.score
#         print "dealer score before",
#         print self.gameObj.dealer.score
        self.gameObj.dealer.play()

        self.newCardNum0 = self.gameObj.dealer.hand[1]
        self.newCardFace0 = self.findFace(self.newCardNum0)
        self.newCardPix0 = QtGui.QPixmap(self.newCardFace0)
        self.dealerCard2.setPixmap(self.newCardPix0)
        dealerCount = 2
        notDone = True
        dealer_cards = len(self.gameObj.dealer.hand)-2
        if dealer_cards < 2:
                pass
        else:
            while dealer_cards > -1:

                self.newCardNum1 = self.gameObj.dealer.hand[dealerCount]
                self.newCardFace1 = self.findFace(self.newCardNum1)
                self.newCardPix1 = QtGui.QPixmap(self.newCardFace1)

                if dealerCount == 2:
                    self.dealerCard3.setPixmap(self.newCardPix1)
                if dealerCount == 3:
                    self.dealerCard4.setPixmap(self.newCardPix1)
                if dealerCount == 4:
                    self.dealerCard5.setPixmap(self.newCardPix1)
                if dealerCount == 5:
                    self.dealerCard6.setPixmap(self.newCardPix1)
                if dealerCount == 6:
                    self.dealerCard7.setPixmap(self.newCardPix1)
                if dealerCount == 7:
                    self.dealerCard8.setPixmap(self.newCardPix1)
                if dealerCount == 8:
                    self.dealerCard9.setPixmap(self.newCardPix1)
                if dealerCount == 9:
                    self.dealerCard10.setPixmap(self.newCardPix1) 
                if dealerCount == 10:
                    self.dealerCard11.setPixmap(self.newCardPix1)
                dealer_cards -= 1


       

        # print "dealer score after",
        # print self.gameObj.dealer.score
        ## next 6 lines added ##
        # if self.gameObj.dealer.score > 21:
        #     print "player wins"
        # elif self.gameObj.dealer.score > self.gameObj.player.score:
        #     print "dealer wins"
        # else:
        #     print "player wins"



    def initGameplayWidget(self):
        self.count = 2
        
        #remove beginning menu layout 
        self.hbox.deleteLater()
        QCoreApplication.sendPostedEvents(self.hbox, QEvent.DeferredDelete)

        self.dealCards = QtWidgets.QPushButton('Deal')
        self.dealCards.clicked.connect(self.deal_cards)
        self.dealCards.setFixedWidth(80)

        self.hit = QtWidgets.QPushButton('Hit')
        self.hit.clicked.connect(self.hit_game)
        self.hit.setFixedWidth(80)

        self.stand = QtWidgets.QPushButton('Stand')
        self.stand.clicked.connect(self.player_stands)
        self.stand.setFixedWidth(80)

        #gameplay layout
        self.dealerBox = QHBoxLayout()
        self.playerBox = QHBoxLayout()
        self.moveBox = QHBoxLayout()
        self.contentBox = QVBoxLayout()



        ## Set card widgets ##
        self.cardBack = QPixmap('CardImgs/back2.jpg')

        self.dealerCard1 = QtWidgets.QLabel()
        self.dealerCard2 = QtWidgets.QLabel()
        self.dealerCard3 = QtWidgets.QLabel()
        self.dealerCard4 = QtWidgets.QLabel()
        self.dealerCard5 = QtWidgets.QLabel()
        self.dealerCard6 = QtWidgets.QLabel()
        self.dealerCard7 = QtWidgets.QLabel()
        self.dealerCard8 = QtWidgets.QLabel()
        self.dealerCard9 = QtWidgets.QLabel()
        self.dealerCard10 = QtWidgets.QLabel()

        self.playerCard1 = QtWidgets.QLabel()
        self.playerCard2 = QtWidgets.QLabel()
        self.playerCard3 = QtWidgets.QLabel()
        self.playerCard4 = QtWidgets.QLabel()
        self.playerCard5 = QtWidgets.QLabel()
        self.playerCard6 = QtWidgets.QLabel()
        self.playerCard7 = QtWidgets.QLabel()
        self.playerCard8 = QtWidgets.QLabel()
        self.playerCard9 = QtWidgets.QLabel()
        self.playerCard10 = QtWidgets.QLabel()
        self.playerCard11 = QtWidgets.QLabel()

        self.updateCards()

        self.dealerCard1.setScaledContents(True)
        self.dealerCard1.setMaximumSize(75,125)
        self.dealerCard2.setScaledContents(True)
        self.dealerCard2.setMaximumSize(75,125)
        self.dealerCard3.setScaledContents(True)
        self.dealerCard3.setMaximumSize(75,125)
        self.dealerCard4.setScaledContents(True)
        self.dealerCard4.setMaximumSize(75,125)
        self.dealerCard5.setScaledContents(True)
        self.dealerCard5.setMaximumSize(75,125)
        self.dealerCard6.setScaledContents(True)
        self.dealerCard6.setMaximumSize(75,125)
        self.dealerCard7.setScaledContents(True)
        self.dealerCard7.setMaximumSize(75,125)
        self.dealerCard8.setScaledContents(True)
        self.dealerCard8.setMaximumSize(75,125)        
        self.dealerCard9.setScaledContents(True)
        self.dealerCard9.setMaximumSize(75,125)
        self.dealerCard10.setScaledContents(True)
        self.dealerCard10.setMaximumSize(75,125)        

        self.playerCard1.setScaledContents(True)
        self.playerCard1.setMaximumSize(75,125)
        self.playerCard2.setScaledContents(True)
        self.playerCard2.setMaximumSize(75,125)
        self.playerCard3.setScaledContents(True)
        self.playerCard3.setMaximumSize(75,125)
        self.playerCard4.setScaledContents(True)
        self.playerCard4.setMaximumSize(75,125)
        self.playerCard5.setScaledContents(True)
        self.playerCard5.setMaximumSize(75,125)
        self.playerCard6.setScaledContents(True)
        self.playerCard6.setMaximumSize(75,125)
        self.playerCard7.setScaledContents(True)
        self.playerCard7.setMaximumSize(75,125)
        self.playerCard8.setScaledContents(True)
        self.playerCard8.setMaximumSize(75,125)
        self.playerCard9.setScaledContents(True)
        self.playerCard9.setMaximumSize(75,125)
        self.playerCard10.setScaledContents(True)
        self.playerCard10.setMaximumSize(75,125)
        self.playerCard11.setScaledContents(True)
        self.playerCard11.setMaximumSize(75,125)

        self.dealerBox.addStretch(.5)
        self.playerBox.addStretch(.5)

        self.dealerBox.addWidget(self.dealerCard1)
        self.dealerBox.addWidget(self.dealerCard2) 
        self.dealerBox.addWidget(self.dealerCard3)
        self.dealerBox.addWidget(self.dealerCard4) 
        self.dealerBox.addWidget(self.dealerCard5)
        self.dealerBox.addWidget(self.dealerCard6) 
        self.dealerBox.addWidget(self.dealerCard7)
        self.dealerBox.addWidget(self.dealerCard8) 
        self.dealerBox.addWidget(self.dealerCard9)
        self.dealerBox.addWidget(self.dealerCard10)   

        self.playerBox.addWidget(self.playerCard1)
        self.playerBox.addWidget(self.playerCard2)
        self.playerBox.addWidget(self.playerCard3)
        self.playerBox.addWidget(self.playerCard4)
        self.playerBox.addWidget(self.playerCard5)
        self.playerBox.addWidget(self.playerCard6)
        self.playerBox.addWidget(self.playerCard7)
        self.playerBox.addWidget(self.playerCard8)
        self.playerBox.addWidget(self.playerCard9)
        self.playerBox.addWidget(self.playerCard10)
        self.playerBox.addWidget(self.playerCard11)

        self.dealerBox.addStretch(.5)
        self.playerBox.addStretch(.5)

        self.message = QtWidgets.QLabel('New Hand, Hit or Stand?')
        self.dealerLabel = QtWidgets.QLabel('Dealer')
        self.playerLabel = QtWidgets.QLabel('Player')        
        self.message.setStyleSheet("font: bold; color: white; font-size:20px; background-position: center")
        self.dealerLabel.setStyleSheet("font: bold; color: white; font-size:16px; background-position: center")
        self.playerLabel.setStyleSheet("font: bold; color: white; font-size:16px; background-position: center")


        self.message.setAlignment(Qt.AlignCenter)
        self.message.setMargin(0)
        self.dealerLabel.setAlignment(Qt.AlignCenter)
        self.playerLabel.setAlignment(Qt.AlignCenter)

        self.moveBox.addWidget(self.dealCards)
        self.moveBox.addWidget(self.hit)
        self.moveBox.addWidget(self.stand)


        self.contentBox.addStretch(.5)
        self.contentBox.addWidget(self.dealerLabel)
        self.contentBox.addLayout(self.dealerBox)
        self.contentBox.addStretch(.5)
        self.contentBox.addWidget(self.playerLabel)        
        self.contentBox.addLayout(self.playerBox)
        self.contentBox.addStretch(.5)        
        self.contentBox.addWidget(self.message)
        self.contentBox.addLayout(self.moveBox)
        self.contentBox.addStretch(.5)


        self.setLayout(self.contentBox)


    def updateCards(self):
        #TODO finish for all possible cards
        self.dealerCard1Num = self.gameObj.dealer.hand[0]
        self.dealerCard1Face = self.findFace(self.dealerCard1Num)
        self.playerCard1Num = self.gameObj.player.hand[0]
        self.playerCard2Num = self.gameObj.player.hand[1]
        self.playerCard1Face = self.findFace(self.playerCard1Num)
        self.playerCard2Face = self.findFace(self.playerCard2Num)
        self.dCard1QPix = QtGui.QPixmap(self.dealerCard1Face)
        self.pCard1QPix = QtGui.QPixmap(self.playerCard1Face)
        self.pCard2QPix = QtGui.QPixmap(self.playerCard2Face)

        self.dealerCard1.setPixmap(self.dCard1QPix)
        self.dealerCard2.setPixmap(self.cardBack)
        self.playerCard1.setPixmap(self.pCard1QPix)
        self.playerCard2.setPixmap(self.pCard2QPix)   


    def set_cards(self):
        self.dealerCard1.clear()
        self.dealerCard2.clear()
        self.dealerCard3.clear()
        self.dealerCard4.clear()
        self.dealerCard5.clear()
        self.dealerCard6.clear()
        self.dealerCard7.clear()
        self.dealerCard8.clear()
        self.dealerCard9.clear()
        self.dealerCard10.clear()               

        self.playerCard1.clear()
        self.playerCard2.clear()
        self.playerCard3.clear()
        self.playerCard4.clear()
        self.playerCard5.clear()
        self.playerCard6.clear()
        self.playerCard7.clear()
        self.playerCard8.clear()
        self.playerCard9.clear()
        self.playerCard10.clear()
        self.playerCard11.clear()

        self.message.setText("")

        self.cardBack = QPixmap('CardImgs/back2.jpg')
        self.dealerCard1Number = self.gameObj.dealer.hand[0]
        self.dealerCard1Facey = self.findFace(self.dealerCard1Number)
        self.playerCard1Number = self.gameObj.player.hand[0]
        self.playerCard2Number = self.gameObj.player.hand[1]
        self.playerCard1Facey = self.findFace(self.playerCard1Number)
        self.playerCard2Facey = self.findFace(self.playerCard2Number)
        self.dCard1QPixy = QtGui.QPixmap(self.dealerCard1Facey)
        self.pCard1QPixy = QtGui.QPixmap(self.playerCard1Facey)
        self.pCard2QPixy = QtGui.QPixmap(self.playerCard2Facey)

        self.dealerCard1.setPixmap(self.dCard1QPixy)
        self.dealerCard2.setPixmap(self.cardBack)
        self.playerCard1.setPixmap(self.pCard1QPixy)
        self.playerCard2.setPixmap(self.pCard2QPixy)


    def findFace(self,n): #n = cardnum tuple
        self.cardNumIndex = -1
        self.spadesImgs = ['2_of_spades.png', '3_of_spades.png', '4_of_spades.png', '5_of_spades.png', '6_of_spades.png', '7_of_spades.png', '8_of_spades.png', '9_of_spades.png', '10_of_spades.png', "jack_of_spades2", "queen_of_spades2", "king_of_spades2", "ace_of_spades"]
        self.heartsImgs = ['2_of_hearts.png', '3_of_hearts.png', '4_of_hearts.png', '5_of_hearts.png', '6_of_hearts.png', '7_of_hearts.png', '8_of_hearts.png', '9_of_hearts.png', '10_of_hearts.png', "jack_of_hearts2", "queen_of_hearts2", "king_of_hearts2", "ace_of_hearts"]
        self.clubsImgs = ['2_of_clubs.png', '3_of_clubs.png', '4_of_clubs.png', '5_of_clubs.png', '6_of_clubs.png', '7_of_clubs.png', '8_of_clubs.png', '9_of_clubs.png', '10_of_clubs.png', "jack_of_clubs2", "queen_of_clubs2", "king_of_clubs2", "ace_of_clubs"]
        self.diamondsImgs = ['2_of_diamonds.png', '3_of_diamonds.png', '4_of_diamonds.png', '5_of_diamonds.png', '6_of_diamonds.png', '7_of_diamonds.png', '8_of_diamonds.png', '9_of_diamonds.png', '10_of_diamonds.png', "jack_of_diamonds2", "queen_of_diamonds2", "king_of_diamonds2", "ace_of_diamonds"]

        self.cardNumIndex = n[0] - 2

        if n[1] == "Spades":
            self.cardFaceFile = self.spadesImgs[self.cardNumIndex]
        elif n[1] == "Hearts":
            self.cardFaceFile = self.heartsImgs[self.cardNumIndex]
        elif n[1] == "Clubs":
            self.cardFaceFile = self.clubsImgs[self.cardNumIndex]
        else: #n[1] == "Diamonds":
            self.cardFaceFile = self.diamondsImgs[self.cardNumIndex]

        self.imgString = "CardImgs/" + self.cardFaceFile
        return self.imgString


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = MainWindow()
    app.exec_()