import numpy.random as npr 
import numpy as np 

def p(x):
    print(x)

#deck creation/shuffle 
deck = npr.choice(52,52, replace=False) #0 = 52
p(deck)
deck = np.where(deck == 0,52,deck)

p(deck)

