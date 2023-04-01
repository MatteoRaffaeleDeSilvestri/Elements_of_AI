
import math
import random

# Generate random mountains                                                                               	 
w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]


def climb(x, h):

    # Keep climbing until we've found a summit
    summit = False
    
    while not summit:
        summit = True
        
        if h[x+5] > h[x] and x + 5 < 100:
            x = x + 1        
            summit = False
        
        elif h[x-5] > h[x] and x - 5 >= 0:
            x = x - 1        
            summit = False
    
    return x

def main(h):

    # Start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)
    return x0, x

if __name__ == "__main__":

    main(h)
