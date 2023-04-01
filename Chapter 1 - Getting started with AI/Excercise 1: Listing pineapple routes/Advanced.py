
def main():

    portnames = ['PAN', 'AMS', 'CAS', 'NYC', 'HEL']

    # This will start the recursion
    routes = permutations(portnames)

    for route in routes:

        # PAN is the port of departure
        if route[0] == 'PAN': 
            print(' '.join(route))

def permutations(ports):
 
    if len(ports) == 0:
        return []
 
    if len(ports) == 1:
        return [ports]
 
    port_list = []
 
    for i in range(len(ports)):
        x = ports[i]
 
        remaining_ports = ports[:i] + ports[i+1:]

        for y in permutations(remaining_ports):
           port_list.append([x] + y)

    return port_list

if __name__ == "__main__":

    main()
