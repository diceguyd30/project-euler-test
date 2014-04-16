from math import sqrt

divisors = 0
test = 1
count = 2
while divisors < 501:
    test += count
    divisors = len([x for x in range(1,int(sqrt(test + 1))) if test % x == 0]) * 2
    count += 1
    
print test