print("Problem 1")
print(sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]))

print(" ")

print("Problem 2")
def fibs(x):
    a, b = 0, 1
    while (a < x):
        yield a
        a,b = b, b+a

print(sum([x for x in fibs(4000000) if x % 2 == 0]))
