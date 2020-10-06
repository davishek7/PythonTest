"""
A positive integer m is a prime product if it can be written as p×q, 
where p and q are both primes.
Write a Python function primeproduct(m) that takes an integer m as input and 
returns True if m is a prime product and False otherwise. 
(If m is not positive, your function should return False.)
"""
from math import sqrt
def primeproduct(m):
    for d1 in range(2,int(sqrt(m)+1)):
        if m%d1==0:
            d2=m/d1
            return is_Prime(d1) and is_Prime(d2)
    return False

def is_Prime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
        
    return True

result=primeproduct(202)
print(result)
