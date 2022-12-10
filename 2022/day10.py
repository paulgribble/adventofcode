# PART 1
#
file = open("day10_input.txt","r")
x = 1
adds = [0]
c = 0
ss = 0
while (c < 240):
    line = file.readline().strip().split(" ")
    if (len(line)==2):
        _,n = line
        n = int(n)
        adds.append(0)
        adds.append(n)
    else:
        adds.append(0)
    x = x + adds.pop(0)
    c = c + 1
    if (c in [20,60,100,140,180,220]):
        ss = ss + (c*x)
file.close()
print(f"Part 1: answer is {ss}")


# PART 2
#

def showcrt(crt):
    for i in range(6):
        for j in range(40):
            ij = (i*40)+j
            print(crt[ij], end="")
        print("")
    print("-")

crt = []
for i in range(240):
    crt.append(".")

file = open("day10_input.txt","r")
x = 1
adds = [0]
c = 0
sprite = 2 # 1-based indexing, center of sprite
while (c < 240):
    print(f"c:{c}, sprite:{sprite}")
    if (c in [sprite-1,sprite,sprite+1]):
        crt[c-1] = '#'
    line = file.readline().strip().split(" ")
    if (len(line)==2):
        _,n = line
        n = int(n)
        adds.append(0)
        adds.append(n)
    else:
        adds.append(0)
    x = x + adds.pop(0)
    sprite = x+1 + (int(c/40)*40)
    c = c + 1
    showcrt(crt)
file.close()

print(f"Part 2: answer is ZKGRKGRK")



