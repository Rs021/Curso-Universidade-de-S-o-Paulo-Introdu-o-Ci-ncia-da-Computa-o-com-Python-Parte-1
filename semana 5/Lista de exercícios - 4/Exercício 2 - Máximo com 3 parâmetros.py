def maximo(a,b,c):

    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c
    
    return a
