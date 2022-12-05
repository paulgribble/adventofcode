# PART 1
#

# load in crate starting configuration
crates = [[],[],[],[],[],[],[],[],[]] # 9 stacks each bottom to top
with open("day05_input.txt", 'r') as file:
    for i in range(9):
        line = next(file).strip('\n')
        for j,c in enumerate(range(0,36,4)):
            if (line[c]=='['):
                crates[j].insert(0,line[c+1])                
    _ = next(file)
    for line in file:
        l = line.split('move ')[1]
        n = int(l.split(' from ')[0])
        l = l.split(' from ')[1].split(' to ')
        nfrom = int(l[0]) - 1 # indexing starts at 0 in Python
        nto = int(l[1]) - 1
        for i in range(n):
            crates[nto].append(crates[nfrom].pop())
ctop = []
for i in range(9):
    ctop.append(crates[i].pop())
print(f"Part 1: top is {''.join(ctop)}")

# PART 2
#
# load in crate starting configuration
crates = [[],[],[],[],[],[],[],[],[]] # 9 stacks each bottom to top
with open("day05_input.txt", 'r') as file:
    for i in range(9):
        line = next(file).strip('\n')
        for j,c in enumerate(range(0,36,4)):
            if (line[c]=='['):
                crates[j].insert(0,line[c+1])                
    _ = next(file)
    for line in file:
        l = line.split('move ')[1]
        n = int(l.split(' from ')[0])
        l = l.split(' from ')[1].split(' to ')
        nfrom = int(l[0]) - 1 # indexing starts at 0 in Python
        nto = int(l[1]) - 1
        tmp = []
        for i in range(n):
            tmp.append(crates[nfrom].pop())
        for i in range(n):
            crates[nto].append(tmp.pop())
ctop = []
for i in range(9):
    ctop.append(crates[i].pop())
print(f"Part 2: top is {''.join(ctop)}")



