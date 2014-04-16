from CommonUtilities import findFactors

abund = []
result = {}

for n in range(1, 28124):
    if not n in result:
        result[n] = 0
    if sum(findFactors(n)) > n:
        abund.append(n)
        for x in abund:
            result[x+n] = 1

print sum([k for (k,v) in result.iteritems() if k < 28124 and v == 0])