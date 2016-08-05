''' game_frame.py '''

## wood.jpg from http://www.textureking.com/content/img/stock/big/DSC_6096.JPG
## redseamless.jpg from http://www.myfreetextures.com/wp-content/uploads/2014/10/seamless-wood3.jpg
## green-gradient.jpg from http://www.technocrazed.com/wp-content/uploads/2015/12/Green-Wallpaper-1.jpg
## jungle-green-grunge-texture.jpg from http://www.texturecrate.com/texture/jungle-green-grunge/
## active.jpg from TODO-Still need this img
## logo.jpg by Jeffrey Campbell TODO-Still need this img
## smpot.jpg from
## medpot.jpg from
## lgpot.jpg from

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

    ## closeEvent from peg_game.py example code ##
    # def closeEvent(self,event):
    #     popup = QuitPopup()
    #     reply = popup.exec_()
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

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

        # self.gp = GameplayWidget(self, self.gameMode, self.gameObj)
        self.preGameInfoSetVisible(False)
        if self.hbox.isEnabled():
            self.hbox.setEnabled(False)

        self.initGame()
        # self.setLayout(self.gp)
        

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
        #TODO change to fit blackjack and THE classes
        if self.gameMode == 1:
            self.gameObj = BlackJack()  
            self.initGameplayWidget()
        else: #gameMode == 2
            self.gameObj = TexasHoldEm()
            gameObj.setNumPlayers(self.numPlayers+2) 
            self.initGameplayWidget()

    def deal_cards(self):
        print "dealing cards"
        print "dealer before",
        print self.gameObj.dealer.hand
        print "player before",
        print self.gameObj.player.hand
        self.gameObj.dealer.shuffle()
        self.gameObj.dealer.deal(self.gameObj.player)
        print "dealer after",
        print self.gameObj.dealer.hand
        print "player after",
        print self.gameObj.player.hand

    def player_hits(self):
        print "player hits"
        print "player score before",
        print self.gameObj.player.score
        self.gameObj.dealer.hit(self.gameObj.player)
        print "player score after",
        print self.gameObj.player.score
        if self.gameObj.player.score > 21:
            print "dealer wins"
            self.deal_cards

    def player_stands(self):
        print "player stands"
        print "player final score",
        print self.gameObj.player.score
        print "dealer score before",
        print self.gameObj.dealer.score
        self.gameObj.dealer.play()
        print "dealer score after",
        print self.gameObj.dealer.score
        if self.gameObj.dealer.score > 21:
            print "player wins"
        elif self.gameObj.dealer.score > self.gameObj.player.score:
            print "dealer wins"
        else:
            print "player wins"

    def initGameplayWidget(self):
        self.setGameplayWidget()
        self.showGameplayWidget()
        
        #remove beginning menu layout 
        self.hbox.deleteLater()
        QCoreApplication.sendPostedEvents(self.hbox, QEvent.DeferredDelete)

        self.dealCards = QtWidgets.QPushButton('Deal')
        self.dealCards.clicked.connect(self.deal_cards)
        self.dealCards.setFixedWidth(80)

        self.hit = QtWidgets.QPushButton('Hit')
        self.hit.clicked.connect(self.player_hits)
        self.hit.setFixedWidth(80)

        self.stand = QtWidgets.QPushButton('Stand')
        self.stand.clicked.connect(self.player_stands)
        self.stand.setFixedWidth(80)

        #gameplay layout
        dealerBox = QHBoxLayout()
        playerBox = QHBoxLayout()
        moveBox = QHBoxLayout()
        contentBox = QVBoxLayout()

        dealerBox.addStretch(.5)
        playerBox.addStretch(.5)

        self.spadesImgs = ['2_of_spades.png', '3_of_spades.png', '4_of_spades.png', '5_of_spades.png', '6_of_spades.png', '7_of_spades.png', '8_of_spades.png', '9_of_spades.png', '10_of_spades.png', "jack_of_spades2", "queen_of_spades2", "king_of_spades2", "ace_of_spades2"]
        self.heartsImgs = ['2_of_hearts.png', '3_of_hearts.png', '4_of_hearts.png', '5_of_hearts.png', '6_of_hearts.png', '7_of_hearts.png', '8_of_hearts.png', '9_of_hearts.png', '10_of_hearts.png', "jack_of_hearts2", "queen_of_hearts2", "king_of_hearts2", "ace_of_hearts2"]
        self.clubsImgs = ['2_of_clubs.png', '3_of_clubs.png', '4_of_clubs.png', '5_of_clubs.png', '6_of_clubs.png', '7_of_clubs.png', '8_of_clubs.png', '9_of_clubs.png', '10_of_clubs.png', "jack_of_clubs2", "queen_of_clubs2", "king_of_clubs2", "ace_of_clubs2"]
        self.diamondsImgs = ['2_of_diamonds.png', '3_of_diamonds.png', '4_of_diamondsades.png', '5_of_diamonds.png', '6_of_diamonds.png', '7_of_diamonds.png', '8_of_diamonds.png', '9_of_diamonds.png', '10_of_diamonds.png', "jack_of_diamonds2", "queen_of_diamonds2", "king_of_diamonds2", "ace_of_diamonds2"]



        self.cardBack = QPixmap('CardImgs/back2.jpg')
            # self.cardLabel.setPixmap(self.cardBack)


        dealerCard1 = QtWidgets.QLabel()
        dealerCard2 = QtWidgets.QLabel()

        playerCard1 = QtWidgets.QLabel()
        playerCard2 = QtWidgets.QLabel()

        dealerCard1.setPixmap(self.cardBack)
        dealerCard2.setPixmap(self.cardBack)
        playerCard1.setPixmap(self.cardBack)
        playerCard2.setPixmap(self.cardBack)

        dealerCard1.setScaledContents(True)
        dealerCard1.setMaximumSize(75,125)

        dealerCard2.setScaledContents(True)
        dealerCard2.setMaximumSize(75,125)

        playerCard1.setScaledContents(True)
        playerCard1.setMaximumSize(75,125)

        playerCard2.setScaledContents(True)
        playerCard2.setMaximumSize(75,125)

        dealerBox.addWidget(dealerCard1)
        dealerBox.addWidget(dealerCard2)

        playerBox.addWidget(playerCard1)
        playerBox.addWidget(playerCard2)

        dealerBox.addStretch(.5)
        playerBox.addStretch(.5)



        #self.testLabel = QtWidgets.QLabel('Hello')
        #self.testLabel.setStyleSheet("font: bold; color: white; font-size:24px; background-position: center")
        
        moveBox.addWidget(self.dealCards)
        moveBox.addWidget(self.hit)
        moveBox.addWidget(self.stand)

        contentBox.addLayout(dealerBox)
        contentBox.addLayout(playerBox)
        contentBox.addLayout(moveBox)

        self.setLayout(contentBox)


        print self.gameObj.dealer.hand[0][0]


        



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

    def showGameplayWidget(self):
        
        pass
        
        
        

        


    def setGameplayWidget(self):
        pass

    # class CardWidget(QtWidgets.QWidget):
    #     # def __init__(self,parent=None): 
    #         # QtWidgets.QWidget.__init__(self, parent)
    #     def __init__(self):
    #         # super(QtWidgets.QWidget).__init__()
    #         QtWidgets.QWidget.__init__(self, parent)

    #         self.cardSuit = ""
    #         self.cardNumber = ""
    #         self.cardBack = QPixmap('CardImgs/back2.jpg')
    #         self.cardLabel = QtWidgets.QLabel()
    #         self.cardLabel.setPixmap(self.cardBack)
    #         self.cardLabel.show()

    #     def setCard(c): #c = a card tuple
    #         self.cardSuit = c[1] #2nd value in card tuple
    #         self.cardNumber = c[0] #1st value in card tuple

    #     def showFront(self,b):
    #         if b == True:   #show front of card
    #             #TODO get cardNumIndex from gameObj?
    #             self.cardNumIndex = -1
    #             if self.cardNumber == "Ace":
    #                 self.cardNumIndex == 12
    #             elif self.cardNumber == "King":
    #                 self.cardNumIndex == 11
    #             elif self.cardNumber == "Queen":
    #                 self.cardNumIndex == 10
    #             elif self.cardNumber == "Jack":
    #                 self.cardNumIndex == 9
    #             else:
    #                 self.cardNumIndex == int(self.cardNumber)

    #             if self.cardSuit == "Spades":
    #                 self.cardLabel.setPixmap(self.spadesImgs[cardNumIndex])
    #             elif self.cardSuit == "Hearts":
    #                 self.cardLabel.setPixmap(self.heartsImgs[cardNumIndex])
    #             elif self.cardSuit == "Clubs":
    #                 self.cardLabel.setPixmap(self.clubsImgs[cardNumIndex])
    #             else: #self.cardSuit == "Diamonds":
    #                 self.cardLabel.setPixmap(self.diamondsImgs[cardNumIndex])                                                
    #         else:   #show card back
    #             self.cardLabel.setPixmap("cardBack.jpg")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = MainWindow()
    app.exec_()