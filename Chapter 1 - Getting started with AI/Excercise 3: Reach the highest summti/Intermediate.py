
import math
import random                        	 

# Generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

h[0] = 0.0
h[99] = 0.0

def climb(x, h):

    # Keep climbing until we've found a summit
    summit = False
    
    while not summit:
        summit = True
        
        if h[x+1] > h[x]:
            x = x + 1        
            summit = False
        
        elif h[x-1] > h[x]:
            x = x - 1        
            summit = False
    
    return x

def main(h):

    # Start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

if __name__ == "__main__":

    main(h)
