import numpy as np

def day2run(oc):
  i = 0
  while (i <= len(oc)-4):
    i1 = oc[i+1]
    i2 = oc[i+2]
    i3 = oc[i+3]
    if (oc[i]==1):
      oc[i3] = oc[i1] + oc[i2]
    elif (oc[i]==2):
      oc[i3] = oc[i1] * oc[i2]
    elif (oc[i]==99):
      break
    i = i + 4
  return oc[0]

# Part 1
opcodes = np.loadtxt("day02_input.txt", dtype=int, delimiter=",")

opcodesp1 = opcodes.copy()
opcodesp1[1] = 12
opcodesp1[2] = 2
p1 = day2run(opcodesp1)
print("Part 1: answer is {:d}".format(p1))

# Part 2
ij = np.zeros((10000,2), dtype=int)
ind = 0
for i in range(99+1):
    for j in range(99+1):
        ij[ind,0] = i
        ij[ind,1] = j
        ind = ind + 1
for i in range(len(ij)):
  opcodesp2 = opcodes.copy()
  opcodesp2[1] = ij[i,0]
  opcodesp2[2] = ij[i,1]
  p2 = day2run(opcodesp2)
  if (p2 == 19690720):
    print("Part 2: answer is {:d}".format(100*ij[i,0]+ij[i,1]))
    break

