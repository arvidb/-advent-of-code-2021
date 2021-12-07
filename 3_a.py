import fileinput


def solve(A, predicate):
    rate = ''
    for x in range(len(A[0])):
        select = '0'
        a = sum(1 if i[x] == '1' else 0 for i in A)
        b = sum(1 if i[x] == '0' else 0 for i in A)
        if predicate(a, b):
            rate += '1'
        else:
            rate += '0'
 
    return int(rate, 2)


A = [list(a[:-1]) for a in fileinput.input()]
print(solve(A, lambda x, y: x > y) * solve(A, lambda x, y: x < y))
