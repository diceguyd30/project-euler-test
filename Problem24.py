def nextPermutation(perm):
    k0 = None
    for i in range(len(perm)-1):
        if perm[i]<perm[i+1]:
            k0=i
    if k0 == None:
        return None

    l0 = k0+1
    for i in range(k0+1, len(perm)):
        if perm[k0] < perm[i]:
            l0 = i

    perm[k0], perm[l0] = perm[l0], perm[k0]
    perm[k0+1:] = reversed(perm[k0+1:])
    return perm

perm=list("0123456789")
i = 0
while i < 999999:
    perm = nextPermutation(perm)
    i += 1
print "".join(perm)