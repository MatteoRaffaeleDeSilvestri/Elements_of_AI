
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Create random data with two classes
X, y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# Scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# Split two data points from the data as test data and use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2)

# Place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# Produce line segments that connect the test data points to the nearest neighbors for drawing the chart
lines = []

# Distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    # Process each of the test data points
    for i, test_item in enumerate(X_test):

        # Calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # Find the index of the nearest neighbor
        nearest_index = min(range(len(distances)), key = distances.__getitem__)

        y_predict[i] = y_train[nearest_index]          
    
    print(y_predict)

if __name__ == "__main__":

    main(X_train, X_test, y_train, y_test)
