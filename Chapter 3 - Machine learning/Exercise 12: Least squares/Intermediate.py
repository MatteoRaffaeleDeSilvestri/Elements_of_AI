
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])

y = np.array([250000, 60000, 525000])

c = np.array([3000, 200, -50, 5000, 100])    # Coefficient values
 
def squared_error(X, y, c):

    sse = 0.0
    
    for x, yi in zip(X, y):

        sse += (yi - x[0]*c[0] + x[1]*c[1] + x[2]*c[2] + x[3]*c[3] + x[4]*c[4])**2
    
    print(sse)

if __name__ == "__main__":

    squared_error(X, y, c)
