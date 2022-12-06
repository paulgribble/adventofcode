# PART 1
#
with open("day06_input.txt", 'r') as file:
    buf = []
    for i in range(4):
        buf.append (file.read(1))
    n = 4
    while (len(set(buf))<4):
        buf.pop(0)
        buf.append(file.read(1))
        n = n + 1
print(f"Part 1: n is {n}")

# PART 2
#
with open("day06_input.txt", 'r') as file:
    buf = []
    for i in range(14):
        buf.append (file.read(1))
    n = 14
    while (len(set(buf))<14):
        buf.pop(0)
        buf.append(file.read(1))
        n = n + 1
print(f"Part 2: n is {n}")





