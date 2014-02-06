from math import sqrt

upperBound = 600851475143
primeList = [2]
test = 3
while test < sqrt(upperBound):
    if not any(test % p == 0 for p in primeList):
        primeList.append(test)
        if upperBound % test == 0:
            upperBound /= test
    test += 2
print upperBound