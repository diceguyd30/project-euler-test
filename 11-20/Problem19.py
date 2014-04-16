import datetime

print sum([1 for x in range(1901, 2001) for y in range(1,13) if datetime.datetime(x, y, 1).weekday() == 1])