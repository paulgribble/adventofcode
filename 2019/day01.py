import numpy as np

# Part 1
m = np.loadtxt("day01_input.txt")
total_fuel = int(np.sum(np.floor(m/3)-2))
print("Part 1: total fuel is {:d}".format(total_fuel))

# Part 2
total_fuel = 0
for i in range(m.shape[0]):
    fm = 0
    f = int(np.floor(m[i]/3)-2)
    while (f > 0):
        fm = fm + f
        f = int(np.floor(f/3)-2)
    total_fuel = total_fuel + fm
print("Part 2: total fuel is {:d}".format(total_fuel))
