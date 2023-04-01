
import numpy as np

x_train = np.random.rand(10, 3)   # Generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # Generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = 0
    min_distance = np.Inf
    index = 0
    min_distance = dist(x_test, x_train[0])
    for i in x_train:
        distance = dist(i, x_test)
        if distance < 0:
            abs(distance)
        if min_distance > distance:
            min_distance = distance
            nearest = index
        index += 1
    print(nearest)

if __name__ == "__main__":

    nearest(x_train, x_test)
