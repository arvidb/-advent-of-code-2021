import fileinput
from collections import defaultdict

grid = defaultdict(int)

for line in fileinput.input():
    a, b = [tuple(map(int, x.split(','))) for x in line.split(' -> ')]
    
    if a[0] == b[0]:
        y0, y1 = min(a[1], b[1]), max(a[1], b[1])
        for i in range(y0, 1+y1):
            grid[a[0], i] += 1
    elif a[1] == b[1]:
        x0, x1 = min(a[0], b[0]), max(a[0], b[0])
        for i in range(x0, 1+x1):
            grid[i, a[1]] += 1
    else:
        dx, dy = a[0] - b[0], a[1] - b[1]
        for ds in range(1+abs(dx)):
            nx = a[0] + (ds if dx < 0 else -ds)
            ny = a[1] + (ds if dy < 0 else -ds)
            grid[nx, ny] += 1

print(len([True for k, v in grid.items() if v > 1]))