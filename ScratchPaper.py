test = 3
upperbound = 100

print map(lambda x: test**2 + (test * x), range(0,((upperbound - test**2) / test) + 1))