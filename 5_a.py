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

print(len([True for k, v in grid.items() if v > 1]))