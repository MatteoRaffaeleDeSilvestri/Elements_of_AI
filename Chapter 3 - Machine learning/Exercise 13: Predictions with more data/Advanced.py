
import numpy as np
from io import StringIO

def fit_model():

    np.set_printoptions(precision = 1)

    # Read the data in and fit it
    x = np.genfromtxt(StringIO(input_string), skip_header = 1)[:,:-1]
    print(x)
    y = np.genfromtxt(StringIO(input_string), skip_header = 1)[:,-1]
    print(y)

    c = np.linalg.lstsq(x, y, rcond = -1)[0]
    
    print(c)
    print(x @ c)

if __name__ == "__main__":

    # Simulate reading a file
    input_string = '''
    25 2 50 1 500 127900
    39 3 10 1 1000 222100
    13 2 13 1 1000 143750
    82 5 20 2 120 268000
    130 6 10 2 600 460700
    115 6 10 1 550 407000
    '''

    fit_model()
