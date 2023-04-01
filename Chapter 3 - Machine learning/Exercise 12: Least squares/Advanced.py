
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])

y = np.array([250000, 60000, 525000])

# Alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):

    best_index = 0
    val_collection = list()

    for coeff in c:
        val_collection.append(X @ coeff)

    coefficient = list()

    for i in np.array(val_collection):
        coefficient.append([(n - j)**2 for n, j in zip(y, i)])
    
    number = sum(coefficient[0])

    for i in coefficient:
        if sum(i) < number:
            number = sum(i)
            best_index = coefficient.index(i)

    print("The best set is set %d" % best_index)

if __name__ == "__main__":
    
    find_best(X, y, c)