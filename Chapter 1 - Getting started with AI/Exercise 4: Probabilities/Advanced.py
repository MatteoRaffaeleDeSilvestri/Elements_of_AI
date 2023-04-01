
import random

def main():

    prob = random.random()
    
    if prob <= 0.1:
        favourite = 'bats'

    elif 0.1 < prob <= 0.2 :
        favourite = 'cats'
    
    else:
        favourite = 'dogs'

    print("I love " + favourite) 

if __name__ == "__main__":
    
    main()
