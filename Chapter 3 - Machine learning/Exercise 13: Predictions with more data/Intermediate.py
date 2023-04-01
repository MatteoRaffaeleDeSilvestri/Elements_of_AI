
import numpy as np

def main(new_cabin, new_cabin_price):
    
    np.set_printoptions(precision = 1)

    x = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600]
        ]
    )   
    
    y = np.array([127900, 222100, 143750, 268000, 460700])
    
    x_new = np.vstack((x, new_cabin))
   
    y_new = np.append(y, new_cabin_price)

    c = np.linalg.lstsq(x_new, y_new, rcond = -1)[0]
    
    print(c)
    print(x_new @ c)

if __name__ == "__main__":

    main([115, 6, 10, 1, 550], 407000)
