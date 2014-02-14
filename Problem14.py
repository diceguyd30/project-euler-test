hist = {1:1}

def PopulateCollatz(n):
    global hist
    if n not in hist:
        if n % 2 == 0:
            hist[n] = PopulateCollatz(n / 2) + 1
        else:
            hist[n] = PopulateCollatz((3*n + 1) / 2) + 2
    return hist[n]

for x in range(1,1000001):
    PopulateCollatz(x)
    
print(max(hist, key=lambda x: hist[x]))