
def flip(n):
    odds = 1.0              # Start with 50% chance of the magic coin (1:1)
    for i in range(n):
        r = 1 / 0.5         # r = P(heads | magic) / P(heads | normal) = 1 / 0.5 = 2
        odds *= r           # Update odds value
    print(odds)

if __name__ == "__main__":
        
    n = 1
    flip(n)
