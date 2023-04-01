
import math, random                           	 
import numpy as np

n = 10000 # Size of the problem: number of possible solutions x = 0, ..., n-1

# Generate random mountains                                                                               	 
def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20)
        w = random.randint(3, int(math.sqrt(n/5)))**2
        s = random.random()
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]

    # Scale the height so that the lowest point is 0.0 and the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high-low) for y in h]
    return h

h = mountains(n)

# Start at a random place
x0 = random.randint(1, n-1)
x = x0

# Keep climbing for 5000 steps
steps = 5000

def main(h, x):
    
    n = len(h)
    
    # Start climbing
    for step in range(steps):
        
        T = 2 * max(0, ((steps - step * 1.2) / steps))**3
        x_new = random.randint(max(0, x-1000), min(n-1, x+1000))

        if h[x_new] > h[x]:
            x = x_new   # If the new position is higher go there
        else:
            if T != 0:
                prob = math.exp(-(h[x] - h[x_new])/T)
                if random.random() <= prob:
                    x = x_new   # Accept worst solution in some cases (based on probability)

    return x

if __name__ =="__main__":
    
    x = main(h, x0)
    print("Ended up at %d, highest point is %d" % (x, np.argmax(h)))
