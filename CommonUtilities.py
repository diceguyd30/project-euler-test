def primes(upperBound):
    primeList = [2]
    yield 2
    test = 3
    while (test < upperBound):
        if not any(test % p == 0 for p in primeList):
            primeList.append(test)
            yield test
        test += 2