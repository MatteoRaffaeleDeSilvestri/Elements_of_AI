
# This data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def all_pairs(data):
    
    # This calls the distance function for all the two-row combinations in the data
    dist = [[sum([abs(i-j) for i, j in zip(row1, row2)]) for row1 in data] for row2 in data]
    print(dist)

if __name__ == "__main__":

    all_pairs(data)
