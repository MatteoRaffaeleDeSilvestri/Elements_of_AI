
import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # Normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # Loaded

def roll(loaded):

    if loaded:
        print("Rolling a loaded die")
        p = p2

    else:
        print("Rolling a normal die")
        p = p1

    # Roll the dice 10 times
    # Add 1 to get dice rolls from 1 to 6 instead of 0 to 5

    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("Rolled %d" % roll)
        
    return sequence

def bayes(sequence):

    odds = 1.0                  # Start with odds 1:1
    
    for roll in sequence:
        if roll == 6:
            r = 0.5 / (1/6)
        else:
            r = 0.1 / (1/6)
        odds *= r
    
    if odds > 1:
        return True
    else:
        return False

if __name__ == "__main__":
  
    sequence = roll(True)
    if bayes(sequence):
        print("I think loaded")
    else:
        print("I think normal")
