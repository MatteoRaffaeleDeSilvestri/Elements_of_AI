
# Input values for three mökkis: 
# - Size [m2], 
# - Size of the sauna [m2], 
# - Distance to water [m], 
# - Number of indoor bathrooms, 
# - Proximity of neighbors [m]

X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# Coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):

    for x in X: 
        print(x[0]*c[0] + x[1]*c[1] + x[2]*c[2] + x[3]*c[3] + x[4]*c[4])


if __name__ == "__main__":

    predict(X, c)