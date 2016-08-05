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

from blackjack import BlackJack

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
            self.gameObj = BlackJack(self.numPlayers+2)  
            self.initGameplayWidget()
        else: #gameMode == 2
            self.gameObj = TexasHoldEm()
            gameObj.setNumPlayers(self.numPlayers+2) 
            self.initGameplayWidget()


    def initGameplayWidget(self):
        self.setGameplayWidget()
        self.showGameplayWidget()
        
        #remove beginning menu layout 
        self.hbox.deleteLater()
        QCoreApplication.sendPostedEvents(self.hbox, QEvent.DeferredDelete)

        self.dealCards = QtWidgets.QPushButton('Deal')
        #self.dealCards.clicked.connect()
        self.dealCards.setFixedWidth(80)

        self.hit = QtWidgets.QPushButton('Hit')
        #self.hit.clicked.connect()
        self.hit.setFixedWidth(80)

        self.stand = QtWidgets.QPushButton('Stand')
        #self.stand.clicked.connect()
        self.stand.setFixedWidth(80)

        #gameplay layout
        dealerBox = QHBoxLayout()
        playerBox = QHBoxLayout()
        moveBox = QHBoxLayout()
        contentBox = QVBoxLayout()

        dealerCard1 = self.CardWidget(self)
        dealerCard2 = self.CardWidget(self)

        playerCard1 = self.CardWidget(self)
        playerCard2 = self.CardWidget(self)

        dealerBox.addWidget(dealerCard1)
        dealerBox.addWidget(dealerCard2)

        playerBox.addWidget(playerCard1)
        playerBox.addWidget(playerCard1)


        #self.testLabel = QtWidgets.QLabel('Hello')
        #self.testLabel.setStyleSheet("font: bold; color: white; font-size:24px; background-position: center")
        
        moveBox.addWidget(self.dealCards)
        moveBox.addWidget(self.hit)
        moveBox.addWidget(self.stand)

        contentBox.addLayout(dealerBox)
        contentBox.addLayout(playerBox)
        contentBox.addLayout(moveBox)

        self.setLayout(contentBox)
        





    def showGameplayWidget(self):
        
        pass
        
        
        

        


    def setGameplayWidget(self):
        pass

    class CardWidget(QtWidgets.QWidget):
        def __init__(self,parent=None): 
            QtWidgets.QWidget.__init__(self, parent)
            self.cardSuit = ""
            self.cardNumber = ""
            self.cardBack = QPixmap('CardImgs/back2.jpg')
            self.cardLabel = QtWidgets.QLabel()
            self.cardLabel.setPixmap(self.cardBack)
            self.cardLabel.show()

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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = MainWindow()
    app.exec_()
