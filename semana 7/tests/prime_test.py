from math import sqrt


def is_prime(n):

   d = 2
   if n <= 1: 
     return False
   
   for i in range(2, int(sqrt(n)) + 1):
     if n % i == 0:
       return False
     
   return True

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(15) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-5) == False