
import numpy as np

# This data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def all_pairs(data):
    
    # This calls the distance function for all the two-row combinations in the data
    dist = [[sum(abs(np.asarray(row1) - np.asarray(row2))) for row1 in data] for row2 in data]
    return dist

def find_nearest_pair(data):
    all = np.array([i for i in all_pairs(data)]).astype('float')
    all[all==0] = np.nan
    print(np.unravel_index(np.nanargmin(all), all.shape))

if __name__ == "__main__":
    
    find_nearest_pair(data)
