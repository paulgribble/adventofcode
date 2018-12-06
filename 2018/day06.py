# Advent of Code 2018 Day 6

# Part One

import numpy as np

points = np.loadtxt("day06_input.txt", delimiter=',')
#points = np.loadtxt("day06_test_input.txt", delimiter=',')
n = np.shape(points)[0]

max_x = np.max(points[:,0])
max_y = np.max(points[:,1])
n_c, n_r = int(max_x), int(max_y)

grid = np.ones(shape=(n_r,n_c)) * -1 # -1 is code for baaaad

for c in range(n_c):
	for r in range(n_r):
		d = np.sum(abs(points - np.array([r,c])), 1) # manhattan
		p_closest = np.argmin(d) # which point is the closest
		if (np.sum(d==d[p_closest]) == 1): # not a tie
			grid[r,c] = p_closest

# nullify infinite-area points
for i in range(n):
	# check if the point has an entry on any of the grid borders
	# if so, KGB its entire area
	if (np.sum(grid[0,:]==i)>0 or np.sum(grid[-1,:]==i)>0 or \
		np.sum(grid[:,0]==i)>0 or np.sum(grid[:,-1]==i)>0):
		grid[grid==i] = -1

# count up total area of each point
max_area = 0
max_area_point = 0
for i in range(n):
	area = np.sum(grid==i)
	if (area > max_area):
		max_area = area
		max_area_point = i

print("Day 6 Part 1: the size of the largest area that isn't infinite is {:d}".format(max_area))

# Part Two

region = 0
for c in range(n_c):
	for r in range(n_r):
		d = np.sum(abs(points - np.array([r,c])))
		if (d < 10000):
			region = region + 1

print("Day 6 Part 2: the size of the region containing all locations which have a total distance to all given coordinatesof less than 10000 is {:d}".format(region))

