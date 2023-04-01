
import random

def main():

    cat_prob = 0.20
    
    if random.random() < cat_prob:
        print('cat')
    
    else:
        print('dog')

if __name__ == "__main__":
    
    main()
