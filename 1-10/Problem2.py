def fibs(targetValue):
    a, b = 0, 1
    while (a < targetValue):
        yield a
        a,b = b, b+a

print(sum([x for x in fibs(4000000) if x % 2 == 0]))