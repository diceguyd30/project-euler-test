from math import sqrt

def primes(upperBound):
    primeList = [2]
    yield 2
    test = 3
    while (test < upperBound):
        if not any(test % p == 0 for p in primeList):
            primeList.append(test)
            yield test
        test += 2
    
target = 600851475143 
print [x for x in primes(sqrt(target)) if target % x == 0][-1]