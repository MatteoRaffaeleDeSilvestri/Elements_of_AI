
import random
import numpy as np

def accept_prob(S_old, S_new, T):

    if S_new > S_old:
        return 1.0

    else:   
        return np.exp(-(S_old - S_new) / T)

def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

if __name__ == "__main__":

    accept(150, 140, 5)
