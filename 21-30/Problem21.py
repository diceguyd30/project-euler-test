from CommonUtilities import findFactors

hist = {}
result = []

for x in range(1,10001):
    temp = sum(findFactors(x))
    if temp in hist and x == hist[temp]:
        result.append(x)
        result.append(temp)
    else:
        hist[x] = temp
        
print sum(result)