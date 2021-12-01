import fileinput

A = list(map(int, fileinput.input()))
B = [sum([x, A[i+1], A[i+2]]) for i, x in enumerate(A) if i < len(A)-2]

print(len([i for i, x in enumerate(B) if i > 0 and x > B[i-1]]))
