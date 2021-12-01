import fileinput

A = list(map(int, fileinput.input()))
print(len([i for i, x in enumerate(A) if i > 0 and x > A[i-1]]))
