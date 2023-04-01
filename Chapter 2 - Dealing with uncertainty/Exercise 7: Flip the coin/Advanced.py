
import numpy as np

# Generate the random list of 1 and 0
def generate(p1):

    seq = np.random.choice([0, 1], p=[1-p1, p1], size=10000)
    return seq

# Count the numbero of five consecutive 1 in the list
def count(seq):

    count = 0

    for i in range(0, len(seq)-4):
        if seq[i] == 1 and seq[i:i+5].tolist() == 5*[1]: 
            count += 1
    
    return count

def main(p1):
    seq = generate(p1)
    return count(seq)

if __name__ == "__main__":

    print(main(2/3))
