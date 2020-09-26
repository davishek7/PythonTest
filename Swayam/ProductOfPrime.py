"""
A positive integer m is a prime product if it can be written as p×q, 
where p and q are both primes.
Write a Python function primeproduct(m) that takes an integer m as input and 
returns True if m is a prime product and False otherwise. 
(If m is not positive, your function should return False.)
"""
def get_factors(m):

    factors=[]

    for i in range(1,m):
        if m%i==0:
            factors.append(i)
    return factors

def prime_check(m):
    if len(get_factors(m))<3:
        return True
    else:
        return False

def primeproduct(m):
    factors=get_factors(m)
    if len(factors)>2 and factors[1]!=2:
        return True
    else:
        return False

result=primeproduct(46)
print(result)
prime=prime_check(6)
print(prime)