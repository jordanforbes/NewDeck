import numpy.random as npr 
import numpy as np 
from util import p 
from CardReader import CardReader as cr
from deck import Deck 

class Player():
    def __init__(self):
        self.hand = []
    
    def showHand():
        p(self.hand)


    
    @staticmethod
    def showCard(name, suit):
        title = f"{name} of {suit}"
        p(title)
        return title


#deck creation/shuffle 



d = Deck()

p("@@@@START@@@@")
for x in range(2):
    d.draw()
d.readHand()
d.shuffle() 
d.draw()
d.readHand()

# cTest = [1,4,9,13,14,26,32,39,21,27,39,40]
# for x in cTest:
#     idCard(x)

# a = np.arange(10) 
# p(a)
# s = a[1:]
# print( a[s])
# p(a)