# PART 1
#
psum = 0
with open("day03_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        n = int(len(line)/2)
        c1, c2 = set(list(line[:n])), set(list(line[n:]))
        i = c1.intersection(c2).pop()
        if i.islower():
            p = ord(i)-96
        else:
            p = ord(i)-38
        psum = psum + p
print(f"Part 1: score is {psum}")

# PART 2
#
psum = 0
g = []
with open("day03_input.txt", 'r') as file:
    e = 0
    for line in file:
        line = line.strip()
        g.append(set(list(line)))
        e = e + 1
        if (e==3):
            i = g[0].intersection(g[1].intersection(g[2])).pop()
            if i.islower():
                p = ord(i)-96
            else:
                p = ord(i)-38
            psum = psum + p
            e = 0
            g = []
print(f"Part 2: score is {psum}")


