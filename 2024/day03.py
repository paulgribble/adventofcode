import re

with open("day03_input.txt") as f:
    data = f.read()

r = 0
for i,j,k in re.findall("(mul\(([0-9]{1,3}),([0-9]{1,3})\))", data):
    r += int(j) * int(k)
print(f"Part 1: {r}")

r = 0
enabled = True
for i,j,k in re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data):
    if (enabled and i[0:3]=='mul'):
        r += int(j) * int(k)
    elif (i[0:3]=='don'):
        enabled = False
    elif (i[0:3]=='do('):
        enabled = True
print(f"Part 2: {r}")
