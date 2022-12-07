# PART 1
#

tree = dict({"root":0}) # name:size list of all directories and sizes
cur  = []               # list of the current directory and its parents

with open("day07_input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        if (line == "$ cd /"):
            cur = ["root"]
        elif (line[0:7] == "$ cd .."): # jump up a directory
            cur.pop()
        elif (line[0:4] == "$ cd"):    # jump down into a directory
            cur.append(cur[-1] + "/" + line[5:]) # add dir to cur list
            tree[cur[-1]] = 0                    # set its size to 0
        elif line[0].isdigit():        # file size
            for fname in cur: # for all dirs in cur list
                fsize = line.split(" ")[0]
                tree[fname] += int(fsize) # add filesize to each

vsum = 0
for v in tree.values():
    if (v <= 100000):
        vsum = vsum + v

print(f"Part 1: answer is {vsum}")


# PART 2
#

vdel = max(tree.values())
for v in tree.values():
    if ((v >= (tree["root"]-40000000)) and (v < vdel)):
        vdel = v

print(f"Part 2: answer is {vdel}")


