import fileinput

A = [(a, int(b)) for a, b in [a.split() for a in fileinput.input()]]
hor = 0
dep = 0
for a, b in A:
    if a == "forward":
        hor += b
    elif a == "down":
        dep += b
    elif a == "up":
        dep -= b

print(hor * dep)
