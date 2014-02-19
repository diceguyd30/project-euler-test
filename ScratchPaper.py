lines = map(lambda x: map(int,x), [l.split() for l in open("problem18.txt")])
print lines
print range(1,15)[::-1]
print max(5,7)