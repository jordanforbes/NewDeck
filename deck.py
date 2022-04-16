
from util import p 
import Imports as I

class Deck():
    deck = I.npr.choice(52, 52, replace=False)  # 0 = 52
    deck = I.np.where(deck == 0, 52, deck)
    hand = []

    def __init__(self):
        p("$$$ Building Deck $$$")
        self.deck = self.deck
        self.showDeck()

# p(deck.item(0))
    def draw(self):
        p("$$$ Drawing Card $$$")
        c = self.deck[0]
        self.addToHand(c)
        cr.idCard(c)
        self.remDeck()
        p()
        self.showHand()
        p()
        self.showDeck()

    def addToHand(self, c):
        p("XXX add to hand XXX")
        self.hand.append(c)

    def remDeck(self, times=1):
        p("XXX remove from deck XXX")
        self.deck = self.deck[times:]

    def remHand(self, times=1):
        p("XXX remove from hand XXX")
        self.hand = self.hand[times:]

    def showDeck(self):
        p("in deck:")
        p(self.deck)
        return self.deck

    def readHand(self):
        handNames = []
        for x in range(len(self.hand)):
            card = cr.idCard(self.hand[x])
            handNames.append(card)
        p(handNames)
        return handNames

    def showHand(self):
        p("in hand:")
        p(self.hand)
        return self.hand

    def shuffle(self):
        npr.shuffle(self.deck)
        self.showDeck()
