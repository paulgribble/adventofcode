import itertools

with open("day08_input.txt") as f:
    F = [list(line.strip()) for line in f.readlines()]

nr = len(F)
nc = len(F[0])

# find antennas
antennas = {}
for i in range(nr):
    for j in range(nc):
        if F[i][j] != '.':
            if F[i][j] not in antennas:
                antennas[F[i][j]] = [(i,j)]
            else:
                antennas[F[i][j]].append((i,j))

antinodes = []
# determine antinodes
for a in antennas:
    for pair in itertools.product(antennas[a], repeat=2):
        if pair[0] != pair[1]:
            dX, dY = pair[1][0]-pair[0][0], pair[1][1]-pair[0][1]
            antinode0 = (pair[0][0]-dX, pair[0][1]-dY)
            if ((antinode0[0]>=0) and (antinode0[0]<nr) and (antinode0[1]>=0) and (antinode0[1]<nc)):
                if (antinode0 not in antinodes):
                    antinodes.append(antinode0)
            antinode1 = (pair[1][0]+dX, pair[1][1]+dY)
            if ((antinode1[0]>=0) and (antinode1[0]<nr) and (antinode1[1]>=0) and (antinode1[1]<nc)):
                if (antinode1 not in antinodes):
                    antinodes.append(antinode1)
print(f"Part 1: {len(antinodes)}")


antinodes = set()

def antinode(pr1, pr2):
    x1, y1 = pr1
    x2, y2 = pr2
    dx,dy = (x2-x1), (y2-y1)
    newx = x2 + dx
    newy = y2 + dy
    antinodes.add((x2,y2))
    while newx >= 0 and newx < nr and newy >= 0 and newy < nc:
        antinodes.add((newx,newy))
        newx += dx
        newy += dy
                
for k in antennas:
    node_list = antennas[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            node1 = node_list[i]
            node2 = node_list[j]
            antinode(node1, node2)
            antinode(node2, node1)


print(f"Part 2: {len(antinodes)}")

