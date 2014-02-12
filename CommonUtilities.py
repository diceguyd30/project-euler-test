from math import sqrt

def primesUntil(upperBound):
    primeList = [2]
    yield 2
    test = 3
    while (test < upperBound):
        if not any(test % p == 0 for p in primeList):
            primeList.append(test)
            yield test
        test += 2
        
def primes():
    primeList = [2]
    yield 2
    test = 3
    while True:
        if not any(test % p == 0 for p in primeList):
            primeList.append(test)
            yield test
        test += 2
        
def primesSieve(upperBound):
    a = [True] * (upperBound + 1)
    for i in range(2, int(sqrt(upperBound))):
        if a[i]:
            for j in map(lambda x: i**2 + (i * x), range(0,((upperBound - i**2) / i) + 1)):
                a[j] = False
    for x in range(2, len(a)):
        if a[x]:
            yield x
    