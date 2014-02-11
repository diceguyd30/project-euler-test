from math import factorial 
from CommonUtilities import primes

def FindSmallestMultiple(n):
    i = reduce(lambda x, y: x*y, primes(20)) * 2
    while True:
        if all([i % x == 0 for x in range(1,n)]):
            return i
        i += 20
            
print(FindSmallestMultiple(20))