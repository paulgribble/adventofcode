import numpy as np
import copy

with open("day06_input.txt") as f:
    m = [list(line.strip()) for line in f.readlines()]

ny = len(m)
nx = len(m[0])

# find the start point ^ (x,y)
i=0
while(i<len(m)):
    if (m[i].count('^') > 0):
        break
    i += 1
y1,x1 = i, m[i].index('^')

def turn_right(direction):
    if (direction==(-1,0)):   # N (rows, cols); (-y,x)
        return (0,1)          # E
    elif (direction==(0,1)):  # E
        return (1,0)          # S
    elif (direction==(1,0)):  # S
        return (0,-1)         # W
    elif (direction==(0,-1)): # W
        return (-1,0)         # N

def inside(x,y,nx,ny):
    return ((x>=0) and (y>=0) and (x<nx) and (y<ny))

visited = {}
direction = (-1,0) # up
y,x = y1,x1
while inside(y,x,ny,nx):
    visited[(y,x)] = True
    yy,xx = (y+direction[0], x+direction[1])
    if (inside(yy,xx,ny,nx) and (m[yy][xx]=='#')):
        direction = turn_right(direction)
    else:
        y,x = yy,xx
n_visited = len(visited.keys())
print(f"Part 1: {n_visited}")


def test_run(obstacle_position):
    mm = copy.deepcopy(m)
    visited = {}
    mm[obstacle_position[0]][obstacle_position[1]] = '#'
    y,x = y1,x1
    direction = (-1,0) # up
    ok = True
    while inside(y,x,ny,nx):
        if (((y,x,direction) in visited.keys()) and (visited[(y,x,direction)] == True)):
            ok = False
            break
        else:
            visited[(y,x,direction)] = True
            yy,xx = (y+direction[0], x+direction[1])
            if (inside(yy,xx,ny,nx) and (mm[yy][xx]=='#')):
                direction = turn_right(direction)
            else:
                y,x = yy,xx
    return ok

o_count = 0
for i in range(ny):
    for j in range(nx):
        if (not ((i==y1) and (j==x1))):
            if (test_run([i,j])==False):
                o_count += 1

print(f"Part 2: {o_count}")
