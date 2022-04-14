import numpy.random as npr 

def p(x):
    print(x)

deck = npr.choice(52,52, replace=False) #0 = 52
p(deck)
npr.shuffle(deck)
p(deck)

