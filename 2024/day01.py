import numpy as np

l = np.genfromtxt("day01_input.txt", delimiter="   ", dtype=int)

# Part 1

l1 = np.sort(l[:,0])
l2 = np.sort(l[:,1])
d = np.sum(np.abs(l2-l1))
print(f"Part 1: {d}")

# Part 2

ss = 0
for i in l1:
    ss = ss + (i * np.sum(i==l2))

print(f"Part 2: {ss}")
