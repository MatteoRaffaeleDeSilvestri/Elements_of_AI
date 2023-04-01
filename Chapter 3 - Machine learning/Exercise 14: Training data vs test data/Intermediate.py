
import numpy as np

def main(test_dataset):

    np.set_printoptions(precision = 1)
    
    x_train = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550 ]
        ]
    )   
    
    y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    x_test = np.array(test_dataset)

    c = np.linalg.lstsq(x_train, y_train, rcond = -1)[0]

    print(x_test @ c)

if __name__ == "__main__":

    test_dataset = [
            [36, 3, 15, 1, 850],
            [75, 5, 18, 2, 540]
        ]

    main(test_dataset)
