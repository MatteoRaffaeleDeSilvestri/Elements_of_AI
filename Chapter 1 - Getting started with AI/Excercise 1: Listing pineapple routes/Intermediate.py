
def main():

    portnames = ['PAN', 'AMS', 'CAS', 'NYC', 'HEL']

    port1 = 0
    
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    
                    # Don't print route with repeted ports
                    if(set(route) == {x for x in range(5)}):
                        print(' '.join([portnames[i] for i in route]))


if __name__ == "__main__":

    main()
