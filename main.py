import numpy.random as npr 
import numpy as np 

def p(x=""):
    print(x)

#deck creation/shuffle 
deck = npr.choice(52,52, replace=False) #0 = 52
hand = []
# p(deck)
deck = np.where(deck == 0,52,deck)
card = 0

p(deck)
# p(deck.item(0))

def draw(d=deck, h=hand):
    card = deck[0]
    h.append(card)
    idCard(card)
    d = d[1:]
    p(d)
    p()
    p("in hand")
    p(h)

def idCard(c):
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
    name = checkFace(v)
    p(f"{name} of {suit}")  
    return (name,suit,c)


def checkFace(n):
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

draw()


# cTest = [1,4,9,13,14,26,32,39,21,27,39,40]
# for x in cTest:
#     idCard(x)

# a = np.arange(10) 
# p(a)
# s = a[1:]
# print( a[s])
# p(a)