
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from scipy import stats

# Create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# Scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# Split two data points from the data as test data and use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# Place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# Distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def main(X_train, X_test, y_train, y_test):

    k = 3    # Classify our test items based on the classes of 3 nearest neighbors
    distances_list = []
    
    for i, test_item in enumerate(X_test):

        distances = [dist(train_item, test_item) for train_item in X_train]
        distances_list.append(distances)

    sort_index = np.argsort(distances_list)
    y_predict = []

    for i in range(len(sort_index)):

        using = sort_index[i][0:k]
        y_train_use = []

        for j in using:

            y_train_use.append(y_train[j])

        m, j = stats.mode(y_train_use)
        y_predict.append(m[0])

    print(np.asarray(y_predict))

if __name__ == "__main__":

    main(X_train, X_test, y_train, y_test)
