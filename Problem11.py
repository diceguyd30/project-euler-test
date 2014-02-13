lines = [l.strip() for l in open("problem11.txt")]
grid = map(lambda x: map(int, x.split(' ')), lines)

def gottaFindEmAll(g):
    for y in range(0,20):
        for x in range(0,17):
            yield [g[y][x], g[y][x+1], g[y][x+2], g[y][x+3]]
            if y < 17:
                yield [g[y][x], g[y+1][x+1], g[y+2][x+2], g[y+3][x+3]]
    for x in range(0,20):
        for y in range(4,20):
            yield [g[y][x], g[y-1][x], g[y-2][x], g[y-3][x]]
            if x <17:
                yield [g[y][x], g[y-1][x+1], g[y-2][x+2], g[y-3][x+3]]
            
print max(map(lambda x: reduce(lambda a,b: a*b, x), gottaFindEmAll(grid)))