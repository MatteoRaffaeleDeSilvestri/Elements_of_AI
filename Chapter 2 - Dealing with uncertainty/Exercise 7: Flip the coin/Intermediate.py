
def count11(seq):

    count = 0

    for i in range(0, len(seq)-1):
        if seq[i] == 1 and seq[i:i+2] == 2*[1]: 
            count += 1
    
    return count

if __name__ == "__main__":

    print(count11([0, 0, 1, 1, 1, 0]))  # Should print 2
