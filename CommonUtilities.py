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
            
            
def findMaxPath(fileName):
    lines = map(lambda x: map(int,x), [l.split() for l in open(fileName)])
    for y in range(1,len(lines))[::-1]:
        for x in range(0,len(lines[y]) - 1):
            lines[y-1][x] += max(lines[y][x], lines[y][x+1])
    return lines[0][0]
    
def findFactors(n):
    s = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            s.add(x)
            if x != 1:
                s.add(n / x)
    return list(s)