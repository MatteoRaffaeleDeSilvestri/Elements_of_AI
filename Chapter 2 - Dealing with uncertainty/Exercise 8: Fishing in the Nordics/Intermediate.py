
def main():

    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    fishers = [1891, 2652, 3800, 11611, 1757]

    for country, fisher in zip(countries, fishers):
        print("%s %.2f%%" % (country, fisher/sum(fishers)*100))

if __name__ == "__main__":
    
    main()
