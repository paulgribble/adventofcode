# PART 1
# used algorithm from here: https://en.wikipedia.org/wiki/Pathfinding

import numpy as np

nr, nc = 41, 61
#nr, nc = 5,8
map = np.zeros((nr, nc))
i=0
with open("day12_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        for j in range(len(line)):
            if line[j]=='E':
                map[i,j] = 26
                E = (i,j)
            elif line[j]=='S':
                S = (i,j)
                map[i,j] = 0
            else:
                map[i,j] = ord(line[j]) - ord('a')
        i += 1

def neighbors(cell):
    n = []
    r,c = cell
    if ((r-1)>=0): n.append((r-1,c))
    if ((r+1)<nr): n.append((r+1,c))
    if ((c-1)>=0): n.append((r,c-1))
    if ((c+1)<nc): n.append((r,c+1))
    return n

cells = dict({E: 0})
finished = False
counter = 0
while (not finished):
    counter += 1
    ck = list(cells.keys())
    ncells = len(ck)
    for i in range(ncells):
        c = ck[i]
        for n in neighbors(c):
            if (((map[c]-map[n])<=1) and (n not in cells.keys())):
                cells.update({n : counter})
    finished = S in cells.keys()

print(f"Part 1: the answer is {cells[S]}")

# PART 2
#

nr, nc = 41, 61
#nr, nc = 5,8
map = np.zeros((nr, nc))
i=0
with open("day12_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        for j in range(len(line)):
            if line[j]=='E':
                map[i,j] = 26
                E = (i,j)
            elif line[j]=='S':
                S = (i,j)
                map[i,j] = 0
            else:
                map[i,j] = ord(line[j]) - ord('a')
        i += 1

def neighbors(cell):
    n = []
    r,c = cell
    if ((r-1)>=0): n.append((r-1,c))
    if ((r+1)<nr): n.append((r+1,c))
    if ((c-1)>=0): n.append((r,c-1))
    if ((c+1)<nc): n.append((r,c+1))
    return n

def shortest_path(S,shortest):
    cells = dict({E: 0})
    finished = False
    counter = 0
    while ((not finished) and (counter < shortest)):
        counter += 1
        ck = list(cells.keys())
        ncells = len(ck)
        for i in range(ncells):
            c = ck[i]
            for n in neighbors(c):
                if (((map[c]-map[n])<=1) and (n not in cells.keys())):
                    cells.update({n : counter})
        finished = S in cells.keys()
    if (counter == shortest):
        return shortest
    else:
        return cells[S]

nump = 0
for ir in range(nr):
    for ic in range(nc):
        if (map[ir,ic]==0):
            nump += 1

shortest = 999
count = 0
for ir in range(nr):
    for ic in range(nc):
        if (map[ir,ic]==0):
            count += 1
            p = shortest_path((ir,ic), shortest)
            if (p < shortest):
                shortest = p
                print(f"searched {count}/{nump} and found new shortest: {p}")

print(f"Part 2: the answer is {shortest}")


