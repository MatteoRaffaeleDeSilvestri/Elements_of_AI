
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):

    guess = None
    biggest = 0.0

    if winner_gender == 'male':

        for country, fisher in zip(countries, male_fishers):
            if guess == None or biggest < fisher/sum(male_fishers)*100:
                guess = country
                biggest = fisher/sum(male_fishers)*100
    
    else:
        
        for country, fisher in zip(countries, female_fishers):
            if guess == None or biggest < fisher/sum(female_fishers)*100:
                guess = country
                biggest = fisher/sum(female_fishers)*100

    return (guess, biggest)  

def main():

    country, fraction = guess("male")
    print("If the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("If the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

if __name__ == "__main__":
    
    main()
