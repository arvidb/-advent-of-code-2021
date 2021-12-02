import fileinput

A = [(x, int(y)) for x, y in [a.split() for a in fileinput.input()]]
hor = 0
aim = 0
dep = 0
for a, b in A:
    if a == "forward":
        hor += b
        dep += aim * b
    elif a == "down":
        aim += b
    elif a == "up":
        aim -= b

print(hor * dep)
