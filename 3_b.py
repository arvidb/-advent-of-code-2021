import fileinput


def solve(A, predicate):
    numbers = A
    for x in range(len(A[0])):
        select = '0'
        a = sum(1 if i[x] == '1' else 0 for i in numbers)
        b = sum(1 if i[x] == '0' else 0 for i in numbers)
        if predicate(a, b):
            select = '1'

        numbers = [a for a in numbers if a[x] == select]
        if (len(numbers) == 1):
            return int(''.join(numbers[0]), 2)


A = [list(a[:-1]) for a in fileinput.input()]
print(solve(A, lambda x, y: x >= y) * solve(A, lambda x, y: x < y))
