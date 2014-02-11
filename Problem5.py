from math import factorial 
from CommonUtilities import primesUntil

def FindSmallestMultiple(n):
    i = reduce(lambda x, y: x*y, primesUntil(20)) * 2
    while True:
        if all([i % x == 0 for x in range(1,n)]):
            return i
        i += 20
            
print(FindSmallestMultiple(20))