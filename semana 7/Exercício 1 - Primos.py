from math import sqrt

def n_primos(n):
    count = 0
    for i in range(2, n):
        prime = True
        print(0)
        for j in range(2, round(sqrt(i)) + 1):
            print(1)
            if i % j == 0:
                prime = False
                break

        if prime:
            count += 1     



    return count
