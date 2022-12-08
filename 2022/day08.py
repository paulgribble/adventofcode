# PART 1
#

import numpy as np

t = np.zeros((0,99))
nrows = 0
with open("day08_input.txt", 'r') as file:
    for line in file:
        line = list(line.strip())
        t = np.vstack([t, np.zeros((1,99))])
        for i,l in enumerate(line):
            t[nrows,i] = int(line[i])
        nrows += 1
n = nrows

#t = np.array([[3,0,3,7,3],
#[2,5,5,1,2],
#[6,5,3,3,2],
#[3,3,5,4,9],
#[3,5,3,9,0]])
#n = 5

visible = set()

for i in range(n):
    visible.add((0,i))
    visible.add((n-1,i))
    visible.add((i,0))
    visible.add((i,n-1))

# rows
for i in range(1,n-1):
    # left->right
    for j in range(1,n-1):
        if all(t[i,0:j] < t[i,j]):
            visible.add((i,j))
    # right->left
    for j in range(n-2,0,-1):
        if all(t[i,j+1:n] < t[i,j]):
            visible.add((i,j))
    
# cols
for i in range(1,n-1):
    # top->bottom
    for j in range(1,n-1):
        if all(t[0:j,i] < t[j,i]):
            visible.add((j,i))
    # bottom->top
    for j in range(n-2,0,-1):
        if all(t[j+1:n,i] < t[j,i]):
            visible.add((j,i))

print(f"Part 1: answer is {len(visible)}")

# PART 2
#

scoremax = 0
for i in range(n):
    for j in range(n):
        adist = 0
        bdist = 0
        ldist = 0
        rdist = 0
        above = t[0:i,   j] < t[i,j]
        below = t[i+1:n, j] < t[i,j]
        left  = t[i,   0:j] < t[i,j]
        right = t[i, j+1:n] < t[i,j]
        k = i-1
        while (k>=0 and k<len(above) and above[k]):
            adist = (i-k)
            k = k - 1
        if (k>0): adist += 1
        k = 0
        while (k<n and k<len(below) and below[k]):
            bdist = (k+1)
            k += 1
        if ((k+i+1)<n): bdist += 1
        k = j-1
        while (k>=0 and k<len(left) and left[k]):
            ldist = (j-k)
            k = k - 1
        if (k>0): ldist += 1
        k = 0
        while (k<n and k<len(right) and right[k]):
            rdist = (k+1)
            k = k + 1
        if ((k+j+1)<n): rdist += 1
        s = adist * bdist * ldist * rdist
        if (s>scoremax):
            scoremax = s

print(f"Part 2: answer is {scoremax}")
