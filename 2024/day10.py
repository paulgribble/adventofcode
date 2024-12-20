with open("day10_input.txt") as f:
    M = [l.strip() for l in f.readlines()]

nr,nc = len(M), len(M[0])

def in_bounds(r,c):
    return ((r>=0) and (c>=0) and (r<nr) and (c<nc))

def trailhead_score(r,c,n):
#    print(f"r,c,n = {r},{c},{n}")
    if (M[r][c]=='9'):
#        print(f"({r},{c})={M[r][c]}")
        if (r,c) not in peaks.keys():
            peaks[(r,c)] = 1
        else:
            peaks[(r,c)] += 1
    else:
        if (in_bounds(r-1,c) and (M[r-1][c]==str(n))): # North
            trailhead_score(r-1,c,n+1)
        if (in_bounds(r,c+1) and (M[r][c+1]==str(n))): # East
            trailhead_score(r,c+1,n+1)
        if (in_bounds(r+1,c) and (M[r+1][c]==str(n))): # South
            trailhead_score(r+1,c,n+1)
        if (in_bounds(r,c-1) and (M[r][c-1]==str(n))): # West
            trailhead_score(r,c-1,n+1)

count = 0
for i in range(nc):
    for j in range(nr):
        if (M[j][i]=='0'):
            peaks = {}
            trailhead_score(j,i,1)
            count += len(peaks)
print(f"Part 1: {count}")

count = 0
for i in range(nc):
    for j in range(nr):
        if (M[j][i]=='0'):
            peaks = {}
            trailhead_score(j,i,1)
            count += sum(peaks.values())
print(f"Part 2: {count}")

