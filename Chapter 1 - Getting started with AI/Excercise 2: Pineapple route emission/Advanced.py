
portnames = ['PAN', 'AMS', 'CAS', 'NYC', 'HEL']

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(ports):

    if len(ports) == 1:
        return [ports]
    
    else:
        port_list = list()
    
        for i in range(len(ports)):
            x = ports[i]
            remaining_ports = ports[:i] + ports[i+1:]
    
            for j in permutations(remaining_ports):
                port_list.append([x]+j)

        return port_list

def main():

    global smallest
    global bestroute

    # Index of the port of departure (PAN)
    start = [0]

    # Generate every possible route
    for combo in permutations(list(range(1, len(portnames)))):
        route = start + combo
        
        # Calculation of the emissions of the route
        lenght = 0
        for i in range(1, len(route)):
            lenght += D[route[i-1]][route[i]]
        
        co2_emission = lenght * co2
        if co2_emission < smallest:
            smallest = co2_emission
            bestroute = route

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

if __name__ == "__main__":

    main()
