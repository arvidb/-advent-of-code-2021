import sys

A = list(map(int, input().split(',')))

best = sys.maxsize
for i in range(max(A)):
    best = min(best, sum([abs(x - i) for x in A]))

print(best)