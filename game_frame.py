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


import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore

class StartFrame(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.createStartFrame()

    ## Load Screen ##
    def createStartFrame(self):
        self.setWindowTitle('Pocket-Aces')
        self.startLayout = StartLayout(self)
        self.setCentralWidget(self.startLayout)
        self.setStyleSheet("QMainWindow { background: 'black'}");

        ## Menu Options ##
        menuBar = self.menuBar().addMenu('File')
        self.newGameOption = menuBar.addAction('New Game')
        self.newGameOption.triggered.connect(self.startLayout.background.newGame)
        self.loadGameOption = menuBar.addAction('Load Game')
        self.loadGameOption.triggered.connect(self.startLayout.background.loadGame)
        self.loadGameOption.setVisible(False)
        self.saveGameOption = menuBar.addAction('Save Game')
        self.saveGameOption.triggered.connect(self.startLayout.background.saveGame)
        self.saveGameOption.setVisible(False)
        self.changeTableOption = menuBar.addAction('Change Table Style')
        self.changeTableOption.triggered.connect(self.changeTableStyle)
        self.exitGameOption = menuBar.addAction('Exit')
        self.exitGameOption.triggered.connect(QtWidgets.qApp.quit)   #could add popup with save option

        self.show()

    def changeTableStyle(self):
        if self.startLayout.background.tStyle == 1:
            self.startLayout.background.tStyle = self.startLayout.background.changeTableStyle(1)
            self.startLayout.background.repaint()
        else:
            self.startLayout.background.tStyle = self.startLayout.background.changeTableStyle(2)
            self.startLayout.background.repaint()

    ## closeEvent from peg_game.py example code ##
    # def closeEvent(self,event):
    #     popup = QuitPopup()
    #     reply = popup.exec_()
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


## Base Layout (level 1) ##
class StartLayout(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self,parent)
        self.setup()

    def setup(self):
        self.background = Background(self)
        self.startLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.startLayout)
        self.startLayout.addWidget(self.background)

## App Start Layout (level 2) ##
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

        ## Inital screen elements ##
        self.newButton = QtWidgets.QPushButton('New Game')
        self.newButton.setToolTip('Begin a new game')
        self.newButton.clicked.connect(self.newGame)
        self.loadButton = QtWidgets.QPushButton('Load Game')
        self.loadButton.setToolTip('Load a previous game')
        self.loadButton.clicked.connect(self.loadGame)
        self.loadButton.setVisible(False)

        ## Game choice screen elements ##
        self.gameModeLabel = QtWidgets.QLabel('Which game will you play?')
        #TODO change color to white and font to bold (and/or larger)
        self.gameModeLabel.setVisible(False)
        self.gameModeCombo = QtWidgets.QComboBox()
        self.gameModeCombo.addItems(['BlackJack','Texas Hold \'Em'])
        self.gameModeCombo.setVisible(False)
        self.playersLabel = QtWidgets.QLabel('How many players (excluding you and the dealer)?')
        #TODO change color to white and font to bold (and/or larger)
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

        self.vbox.addStretch(.5)
        self.vbox.addWidget(self.newButton)
        self.vbox.addWidget(self.loadButton)
        self.vbox.addWidget(self.gameModeLabel)
        self.vbox.addWidget(self.gameModeCombo)
        self.vbox.addWidget(self.playersLabel)
        self.vbox.addLayout(self.comboBoxLayout)        
        self.vbox.addStretch(.5)

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

        ## Pocket Aces Logo ##
        #TODO change to QLabel and add to a layout
        image = QtGui.QImage('logo.jpg')
        qp.drawImage(200,100,image)

        qp.end()

    def changeTableStyle(self, tableStyle):
        if tableStyle == 1:
            return 2
        else: #tableStyle == 2
            return 1

    def newGame(self):
        print("New Game triggered") #Both the newGameOption and newButton lead here
        if self.newButton.isVisible():
            self.newButton.setVisible(False)
        else: #currently in a game, reachable by the new game menu option
            pass
            #check with player to save game
            #hide gameplay layout
            #AND/OR set self.hbox as the current layout (central widget?)
        self.preGameInfoSetVisible(True)



    def loadGame(self):
        print("background.loadGame triggered")
    #     #open loadPopup

    def saveGame(self):
        print("background.saveGame triggered")

    def getNumPlayers(self):
        self.numPlayers = self.playersCombo.currentIndex() + 1
        print self.numPlayers
        self.gameMode = self.gameModeCombo.currentIndex() + 1

        self.gp = Gameplay
        self.preGameInfoSetVisible(False)
        self.gameSetVisible(True)

        # self.setCentralWidget(self.gp)
        

    def preGameInfoSetVisible(self,b):
        self.gameModeLabel.setVisible(b)
        self.gameModeCombo.setVisible(b)
        self.playersLabel.setVisible(b)
        self.playersCombo.setVisible(b)
        self.playersComboOk.setVisible(b)

    def gameSetVisible(self,b):
        self.gp.setVisible(b)

class Gameplay(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self, parent)
        #TODO change to fit blackjack and THE classes
        if gameMode == 1:
            self.gameObj = BlackJack()
        else: #gameMode == 2
            self.gameObj = TexasHoldEm()
        self.setGameplayLayout()
        self.genericPlayerSlots = [[1,3],[2,3],[1,2],[1.1]]
        self.dealerSlot = [1,2]
        self.humanPlayerSlot = [2,3]
        # self.parent.parent.saveGameOption.setVisible(True) #activate save game option in file menu


        #TODO add getHumanPlayer, getDealer, and getGenericPlayers to game classes
        self.playerWidgetList = []
        self.humanPlayerWidget = PlayerWidget()#init human player
        self.humanPlayerWidget.setPlayerObj(self.gameObj.getHumanPlayer())
        self.playerWidgetList.append(self.humanPlayerWidget)
        self.dealerPlayerWidget = PlayerWidget()#init dealer
        self.dealerPlayerWidget.setPlayerObj(self.gameObj.getDealer())
        self.playerWidgetList.append(self.dealerPlayerWidget)        
        self.genericPlayerList = self.gameObj.getGenericPlayers()
        for i in range(len(self.genericPlayerList)):    #init generic players
            self.genericPlayerWidget = PlayerWidget()
            self.genericPlayerWidget.setPlayerObj(self.genericPlayerList[i])
            self.playerWidgetList.append(self.genericPlayerWidget)


    def setGameplayLayout(self):
        self.gameplayLayout = QtWidgets.QGridLayout()
        self.middleGameplayLayout = QtWidgets.QVBoxLayout()
        self.communityCardsWidget = self.CommunityCardsWidget()
        #TODO add getCommunityCards() to game classes
        self.communityCardsWidget.setPlayerObj(self.gameObj.getCommunityCards())
        self.potLayout = BetPotLayout()
        self.potLayout.update()

        #TODO add items to middleGameplayLayout - communityCardsWidget,BetPlotWidget, and if gameMode == 2, winningHandRankingsLabel
        self.middleGameplayLayout.addLayout(self.communityCardsWidget)
        self.middleGameplayLayout.addLayout(self.potLayout)
        #winningHandRankings text from http://www.thepokerpractice.com/how_to_play/
        if self.gameMode == 2:
            self.winningHandRankings =  "Straight Flush - Five cards of the same suit in consecutive order\nFour of a Kind - Four cards of the same value\nFull House - A combination of three of a kind and a pair\nFlush - Any five cards of the same suit\nStraight - Five cards in consecutive order, suit irrelevant\nThree of a Kind - Three cards of the same value\nTwo Pair - Two sets of two cards of the same value\nOne Pair - Two cards of the same value\nHigh Card - The one card with the highest value"
            self.winningHandRankingsLabel = QtWidgets.QLabel(self.winningHandRankings)
            self.middleGameplayLayout.addWidget(self.winningHandRankings)

        self.gameplayLayout.addWidget(self.humanPlayerWidget,humanPlayerSlot[0],humanPlayerSlot[1]) #insert human player into layout
        self.gameplayLayout.addWidget(self.dealerPlayerWidget,dealerSlot[0],dealerSlot[1])#insert dealer into layout
        #insert generic players into layout
        for i in range(len(self.genericPlayerList)):
            self.gameplayLayout.addWidget(self.playerWidgetList[i+2],self.genericPlayerSlots[i][0],self.genericPlayerSlots[i][1])
        self.gameplayLayout.addLayout(middleGameplayLayout,2,2) #insert middleGameplayLayout

        #remove all layouts from background OR just set gameplayLayout as current widget
        self.setCentralWidget(self.gameplayLayout)


class PlayerWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        self.playerObj = None
        self.handCardWidgets = [] #list of cards
        self.playerNameLabel = QtWidgets.QLabel()
        self.currentPlayerIcon = QtWidgets.QLabel.setPixmap(QPixmap("active.jpg"))
        self.setCurrentPlayerIconVisibility(False)
        self.moneyLeftLabel = QtWidgets.QLabel()
        self.playerLayout = QtWidgets.QGridLayout()
        self.playerHeaderLayout = QtWidgets.QHBoxlayout()
        self.handLayout = QtWidgets.QHBoxlayout()

        ## Set Sub-layouts ##
        self.playerHeaderLayout.addWidget(self.currentPlayerIcon)
        self.playerHeaderLayout.addWidget(self.playerNameLabel)
        for x in self.handCardWidgets:
            self.handLayout.addWidget(x)

        ## Set Player Layout ##
        self.playerLayout.addLayout(self.playerHeaderLayout)
        self.playerLayout.addLayout(self.handLayout)
        self.playerLayout.addWidget(self.moneyLeftLabel)

    def setPlayerObj(self,player):
        self.playerObj = player
        self.update()

    def update(self):
        ## Update widgets with player info ##
        self.setPlayerNameLabel()
        self.updateHand()        
        self.setMoneyLeftLabel() 

    def setCurrentPlayerIconVisibility(self, b):
        self.currentPlayerIcon.setVisible(b)

    def setPlayerNameLabel(self,n):
        self.playerNameLabel.setText(self.playerObj.getName())

    def updateHand(self):
        i=0
        for x in self.playerObj.hand:
            self.handCardWidgets.append(CardWidget())
            self.handCardWidgets[i].setCard(x)
            i += 1

    def setCard(self,cnum):
        self.card.setCard(cnum)

    def setMoneyLeftLabel(self):
        self.moneyLeftLabel.setText(self.playerObj.getMoney())

class CommunityCardsWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        self.playerObj = None
        self.handCardWidgets = [] #list of cards

    def setPlayerObj(self,player):
        self.playerObj = player
        self.updateHand()        

    def updateHand(self):
        i=0
        for x in self.playerObj.hand:
            self.handCardWidgets.append(CardWidget())
            self.handCardWidgets[i].setCard(x)
            i += 1

    #TODO edit this to take a tuple
    def setCard(self,cnum):
        self.card.setCard(cnum)    

class CurrentBetWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        self.currentBet = -1
        self.currentBetWidget = QtWidgets.QLabel()
        self.update

    def update(self,event):
        #TODO implement getCurrentBet in game classes
        self.currentBet = self.gameObj.getCurrentBet #get current bet from gameplay class
        self.currentBetWidget.setText('$' + str(self.currentBet))#set current bet amount
        self.repaint

class PotWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        self.currentPotStyle = -1
        self.currentPotWidget = QtWidgets.QLabel()    #or QtGui.QLabel()?
        self.update

    def update(self,event):
        #TODO determine pot amount benchmarks and add to code block
        #TODO get pot images
        #TODO add getPot to gameplay class
        self.currentPot = self.gameObj.getPot()
        if self.currentPot <= 500:
            self.currentPotWidget.setPixmap(QPixmap("smpot.jpg"))#set current bet amount
        elif self.currentPot >500 and self.currentPot <=2000 :
            self.currentPotWidget.setPixmap(QPixmap("medpot.jpg"))
        else: # self.currentPot >2000
            self.currentPotWidget.setPixmap(QPixmap("lgpot.jpg"))                        
        self.repaint

class BetPotLayout(QtWidgets.QWidget):
    def __init__(self,parent):
        bpLayout = QtWidgets.QHBoxlayout()
        bWidget = CurrentBetWidget()
        pWidget = PotWidget()
        bpLayout.addWidget(bWidget)
        bpLayout.addWidget(pWidget)

    def update(self):
        bWidget.update()
        pWidget.update()

class CardWidget(QtWidgets.QWidget):
    def __init__(self,parent):  
        self.cardSuit = ""
        self.cardNumber = ""
        self.cardLabel = QtWidgets.QLabel()
        self.cardLabel.setPixmap("cardBack.jpg")

    def setCard(c): #c = a card tuple
    #TODO get card suit and number from the card tuple
        # self.cardSuit = c. #2nd value in card tuple
        # self.cardNumber = c. #1st value in card tuple
        pass

    def showFront(self,b):
        if b == True:   #show front of card
            #TODO get cardNumIndex from gameObj?
            cardNumIndex = -1
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
    

# class QuitPopup(QtWidgets.QMessageBox):
#     def __init__(self,parent):
#         QtWidgets.QMessageBox.__init__(self,parent)
#         self.setText('Exit the game?')
#         self.clicked.connect(QtWidgets.qApp.quit)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = StartFrame()
    app.exec_()
