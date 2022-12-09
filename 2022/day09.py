# PART 1
#

import numpy as np

def dist(h,t):
    return np.sqrt((h[0]-t[0])**2 + (h[1]-t[1])**2)

def bestmove(h,t):
    moves = np.array([[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]])
    n,_ = np.shape(moves)
    d = np.zeros(n)
    for i in range(n):
        d[i] = dist(h,t+moves[i,:])
    return moves[np.argmin(d),:]

def showboard(h,t):
    for y in range(4,-1,-1):
        for x in range(5):
            c = '.'
            if ((x==0) and (y==0)):
                c = 's'
            if ((t[0]==x) and (t[1]==y)):
                c = 'T'
            if ((h[0]==x) and (h[1]==y)):
                c = 'H'
            print(c, end="")
            if (x==4):
                print('\n', end="")
    print('\n', end="")

h = np.array([0,0])
t = np.array([0,0])
visited = dict({tuple(t): 1})
#showboard(h,t)
eps = np.sqrt(2) + 1e-5
with open("day09_input.txt", 'r') as file:
    for line in file:
        d,n = line.strip().split(" ")
        n = int(n)
        if (d=='L'):
            move = np.array([-1,0])
        elif (d=='R'):
            move = np.array([1,0])
        elif (d=='U'):
            move = np.array([0,1])
        elif (d=='D'):
            move = np.array([0,-1])
        for i in range(n):
            h = h + move
            if (dist(h,t) > eps):
                t = t + bestmove(h,t)
                if tuple(t) in visited.keys():
                    visited[tuple(t)] = visited[tuple(t)] + 1
                else:
                    visited.update({tuple(t): 1})
#            showboard(h,t)

print(f"Part 1: answer is {len(visited)}")

# PART 2
#

h = np.array([0,0])
t = np.zeros((9,2))
visited = dict({tuple(t[8,:]): 1})
#showboard(h,t)
eps = np.sqrt(2) + 1e-5
with open("day09_input.txt", 'r') as file:
    for line in file:
        d,n = line.strip().split(" ")
        n = int(n)
        if (d=='L'):
            move = np.array([-1,0])
        elif (d=='R'):
            move = np.array([1,0])
        elif (d=='U'):
            move = np.array([0,1])
        elif (d=='D'):
            move = np.array([0,-1])
        for i in range(n):
            h = h + move
            if (dist(h,t[0,:]) > eps):
                t[0,:] = t[0,:] + bestmove(h,t[0,:])
            for j in range(1,9):
                if (dist(t[j-1,:],t[j,:]) > eps):
                    t[j,:] = t[j,:] + bestmove(t[j-1,:],t[j,:])
            if tuple(t[8,:]) in visited.keys():
                visited[tuple(t[8,:])] = visited[tuple(t[8,:])] + 1
            else:
                visited.update({tuple(t[8,:]): 1})
#            showboard(h,t)

print(f"Part 2: answer is {len(visited)}")

