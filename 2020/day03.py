with open("day03_input.txt") as f:
	grid= [line.strip('\n') for line in f]

def num_trees(right, down, grid):
	trees,r,c = 0,0,0
	rows, cols = len(grid), len(grid[0])
	while r < rows:
		if grid[r%rows][c%cols] == '#':
			trees += 1
		r += down
		c += right
	return trees	

print("Part 1: {}".format(num_trees(3,1,grid)))

t1 = num_trees(1,1,grid)
t2 = num_trees(3,1,grid)
t3 = num_trees(5,1,grid)
t4 = num_trees(7,1,grid)
t5 = num_trees(1,2,grid)

print("Part 2: {}".format(t1*t2*t3*t4*t5))

