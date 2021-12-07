from collections import deque

A = list(map(int, input().split(',')))

s = deque([0]*9)
for a in A:
    s[a] += 1

for day in range(256):
    tmp = s[0]
    s.rotate(-1)
    s[6] += tmp
    s[8] = tmp

print(sum(s))
