hist = {(0,0): 0}

def findPaths(n):
    return findPathsHelper(n, n)
    
def findPathsHelper(d, r):
    global hist
    if (d,r) in hist:
        return hist[(d,r)]
    elif d == 0:
        return 1
    elif r == 0:
        return 1
    else:
        t = findPathsHelper(d-1,r) + findPathsHelper(d,r-1)
        hist[(d,r)] = t
        return t

print(findPaths(20))