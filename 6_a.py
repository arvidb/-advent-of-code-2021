
A = list(map(int, input().split(',')))

for day in range(80):
    for i, a in enumerate(A):
        if a > 0:
            A[i] -= 1
        else:
            A[i] = 6
            A.append(9)

print(len(A))
        