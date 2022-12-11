# PART 1
#

# load in the monkeys
#
nmonkeys = 8
file = open("day11_input.txt", 'r')

M = []
for i in range(nmonkeys):
    monkey = dict({})
    line = file.readline() # monkey number
    line = file.readline().strip().split(" ")
    line.pop(0)
    line.pop(0)
    items = []
    for j in line:
        items.append(int(j.replace(',','')))
    monkey.update({"items": items.copy()})
    line = file.readline().strip().split(": ")
    line = line[1].split("new = old ")
    op,n = line[1].split(" ")
    monkey.update({"operation": [op,n]})
    _,n = file.readline().strip().split("Test: divisible by ")
    monkey.update({"test": int(n)})
    n = int(file.readline().strip()[-1])
    monkey.update({"true": n})
    n = int(file.readline().strip()[-1])
    monkey.update({"false": n})
    M.append(monkey.copy())
    line = file.readline()
file.close()

activity = [0] * nmonkeys
for i in range(20): # 20 rounds
    for im in range(nmonkeys):
        m = M[im]
        nitems = len(m["items"])
        while (len(m["items"]) > 0):
            j = m["items"][0]
            o = m["operation"][0]
            w = m["operation"][1]
            if w.isdigit():
                w = int(w)
            else:
                w = j
            if o=="*":
                w = j * w
            elif o=="+":
                w = j + w
            w = int(w / 3)
            if ((w % m["test"])==0):
                mto = m["true"]
            else:
                mto = m["false"]
            M[mto]["items"].append(w)
            m["items"].pop(0)
            activity[im] += 1

activity.sort(reverse=True)
print(f"Part 1: answer is {activity[0]*activity[1]}")

# PART 2
#

# load in the monkeys
#
nmonkeys = 8
file = open("day11_input.txt", 'r')

M = []
mfac = 1
for i in range(nmonkeys):
    monkey = dict({})
    line = file.readline() # monkey number
    line = file.readline().strip().split(" ")
    line.pop(0)
    line.pop(0)
    items = []
    for j in line:
        items.append(int(j.replace(',','')))
    monkey.update({"items": items.copy()})
    line = file.readline().strip().split(": ")
    line = line[1].split("new = old ")
    op,n = line[1].split(" ")
    monkey.update({"operation": [op,n]})
    _,n = file.readline().strip().split("Test: divisible by ")
    monkey.update({"test": int(n)})
    mfac = mfac * int(n)
    n = int(file.readline().strip()[-1])
    monkey.update({"true": n})
    n = int(file.readline().strip()[-1])
    monkey.update({"false": n})
    M.append(monkey.copy())
    line = file.readline()
file.close()

activity = [0] * nmonkeys
for i in range(10000): # 10000 rounds
    for im in range(nmonkeys):
        m = M[im]
        nitems = len(m["items"])
        while (len(m["items"]) > 0):
            j = m["items"][0]
            o = m["operation"][0]
            w = m["operation"][1]
            if w.isdigit():
                w = int(w)
            else:
                w = j
            if o=="*":
                w = j * w
            elif o=="+":
                w = j + w
            w = int(w) % mfac
            if ((w % m["test"])==0):
                mto = m["true"]
            else:
                mto = m["false"]
            M[mto]["items"].append(w)
            m["items"].pop(0)
            activity[im] += 1

activity.sort(reverse=True)
print(f"Part 2: answer is {activity[0]*activity[1]}")


