with open("day05_input.txt") as f:
    data = [line.strip() for line in f.readlines()]

i = 0
before = {}
after = {}
while (data[i] != ''):
    r = data[i].split('|')
    r0,r1 = r[0], r[1]
    if r1 in before.keys():
        before[r1].append(r0)
    else:
        before[r1] = [r0]
    if r0 in after.keys():
        after[r0].append(r1)
    else:
        after[r0] = [r1]
    i += 1

updates = data[i+1:]

mids = 0
for u in updates:
    ok = True
    ul = u.split(',')
    for i in range(len(ul)):
        for j in range(len(ul)):
            if (i<j):
                if ((ul[i] in before.keys()) and (ul[j] in before[ul[i]])):
                    ok = False
    if ok:
        mid = int((len(ul))/2)
        mids += int(ul[mid])

print(f"Part 1: {mids}")

mids = 0
for u in updates:
    ok = True
    ul = u.split(',')
    for i in range(len(ul)):
        for j in range(len(ul)):
            if (i<j):
                if ((ul[i] in before.keys()) and (ul[j] in before[ul[i]])):
                    ok = False
                    ul[i],ul[j] = ul[j],ul[i]
    if (ok==False):
        mid = int((len(ul))/2)
        mids += int(ul[mid])

print(f"Part 2: {mids}")


