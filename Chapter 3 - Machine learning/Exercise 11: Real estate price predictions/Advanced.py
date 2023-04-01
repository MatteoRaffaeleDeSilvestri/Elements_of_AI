# Input values for three mökkis: 
# size, size of sauna, distance to water, 
# number of indoor bathrooms, proximity of neighbors

X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

c = [3000, 200, -50, 5000, 100]    # Coefficient values

def predict(X, c):
        
    for data in X:
        price = 0
        index = 0
        for coeff in c:
            price += data[index] * coeff
            index += 1
        print(price)

if __name__ == "__main__":
    
    predict(X, c)
