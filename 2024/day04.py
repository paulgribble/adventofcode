import numpy as np

with open("day04_input.txt") as f:
    w = np.array([list(line.strip()) for line in f.readlines()])

slices = [
    ((0, 0), (1, 0), (2, 0), (3, 0)), # horizontal
    ((0, 0), (0, 1), (0, 2), (0, 3)), # vertical
    ((0, 0), (1, 1), (2, 2), (3, 3)), # diagonal
    ((0, 3), (1, 2), (2, 1), (3, 0)), # other diagonal
]
variants = ['XMAS','SAMX']

[r,c] = np.shape(w)

count = 0
for y in range(r):
    for x in range(c):
        for slice in slices:
            try:
                word = ''.join([w[y + dy][x + dx] for dx,dy in slice])
                if word in variants:
                    count += 1
            except:
                pass
print(f"Part 1: {count}")

slices = [
    ((0, 0), (1, 1), (2, 2), (0, 2), (2, 0)), # x-shape
]
variants = ['MASMS', 'SAMSM', 'MASSM', 'SAMMS']
count = 0
for y in range(r):
    for x in range(c):
        for slice in slices:
            try:
                word = ''.join([w[y + dy][x + dx] for dx,dy in slice])
                if word in variants:
                    count += 1
            except:
                pass
print(f"Part 2: {count}")



