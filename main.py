import numpy.random as npr 
import numpy as np 

def p(x=""):
    print(x)

#deck creation/shuffle 
class Deck():
    deck = npr.choice(52, 52, replace=False)  # 0 = 52
    deck = np.where(deck == 0, 52, deck)
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
        self.idCard(c)
        self.remDeck()
        p()
        self.showHand()
        p()
        self.showDeck()


    def idCard(self,c):
        # p(c)
        v=0
        suit = ""

        if c <=13:
            v = c
            suit = "Hearts"
            
        elif 13 < c <= 26:
            v = c-13
            suit = "Diamonds"

        elif 26 < c <= 39:
            v = c-26
            suit = "Spades"

        elif 39 < c: 
            v = c- 39
            suit = "Clubs"
        name = self.checkFace(v)
        p(f"{name} of {suit}")  
        return (name,suit,c)

    def checkFace(self,n):
        if n == 1:
            return "Ace"
        elif n == 11:
            return "Jack"
        elif n == 12:
            return "Queen"
        elif n == 13:
            return "King"
        else: 
            return n

    def addToHand(self,c):
        p("XXX add to hand XXX")
        self.hand.append(c)

    def remDeck(self,times=1):
        p("XXX remove from deck XXX")
        self.deck= self.deck[times:]
    
    def remHand(self,times=1):
        p("XXX remove from hand XXX")
        self.hand= self.hand[times:]
    
    def showDeck(self):
        p("in deck:")
        p(self.deck)
        return self.deck

    def showHand(self):
        p("in hand:")
        p(self.hand)
        return self.hand


d = Deck()

for x in range(5):
    d.draw()

# cTest = [1,4,9,13,14,26,32,39,21,27,39,40]
# for x in cTest:
#     idCard(x)

# a = np.arange(10) 
# p(a)
# s = a[1:]
# print( a[s])
# p(a)