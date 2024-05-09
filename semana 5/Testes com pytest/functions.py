def factorial(n):
    if n < 1:
        return 1
    total = n
    while n>1:
        n-=1
        total *= n

    return total

def binominal(n,p):

    return factorial(n) // factorial(n - p) // factorial(p)


    assert binominal(9,8) == 9
    assert binominal(7,4) == 35