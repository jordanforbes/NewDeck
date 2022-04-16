from deck import Deck
from util import p 

class CardReader():
    @staticmethod
    def idCard(c):
            # p(c)
        v = 0
        suit = ""

        if c <= 13:
            v = c
            suit = "Hearts"

        elif 13 < c <= 26:
            v = c-13
            suit = "Diamonds"

        elif 26 < c <= 39:
            v = c-26
            suit = "Spades"

        elif 39 < c:
            v = c - 39
            suit = "Clubs"
        name = self.checkFace(v)
        self.showCard(name, suit)
        return (name, suit, v, c)

    @staticmethod
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