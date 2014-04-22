lines = sorted(open("21-30/problem22.txt").read().replace('"', '').split(","))
sums = map(lambda x: sum(map(lambda y: ord(y) - 64, x)), lines)

result = 0
for x in range(1, len(sums) + 1):
    result += (x * sums[x-1])
    
print result