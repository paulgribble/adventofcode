
def turnleft(heading):
	if (heading=='N'):
		return 'W'
	elif (heading=='S'):
		return 'E'
	elif (heading=='W'):
		return 'S'
	elif (heading=='E'):
		return 'N'

def turnright(heading):
	if (heading=='N'):
		return 'E'
	elif (heading=='S'):
		return 'W'
	elif (heading=='W'):
		return 'N'
	elif (heading=='E'):
		return 'S'

def turnreverse(heading):
	if (heading=='N'):
		return 'S'
	elif (heading=='S'):
		return 'N'
	elif (heading=='W'):
		return 'E'
	elif (heading=='E'):
		return 'W'

def move(x,y,heading):
	if (heading=='N'):
		x = x - 1
	elif (heading=='S'):
		x = x + 1
	elif (heading=='W'):
		y = y - 1
	elif (heading=='E'):
		y = y + 1
	return x,y

def printgrid(grid,x,y):
	for i in range(-5,5,1):
		for j in range(-5,5,1):
			if ((i==x) & (j==y)):
				print('* ', end='')
			else:
				if ((i,j) in grid.keys()):
					print('{} '.format(grid[(i,j)]), end='')
				else:
					print('. ', end='')
		print('\n')


# Part 1

lines = [l.strip('\n') for l in open('day22_input.txt')]

# represent the infinite grid as a dictionary
grid = {}
for i in range(len(lines)): # rows
	for j in range(len(lines[i])): # cols
		grid[(i,j)] = lines[i][j] # so grid([x,y]) is horiz,vert


heading = 'N'	# N,S,E,W
x,y = 12,12		# starting position

count = 0 # keep track of number of infections
n = 10000
for i in range(n):
	if (((x,y) in grid.keys()) == False):
		grid[(x,y)] = '.'
	if (grid[(x,y)] == '#'):
		heading = turnright(heading)
		grid[(x,y)] = '.'
	elif (grid[(x,y)] == '.'):
		heading = turnleft(heading)
		grid[(x,y)] = '#'
		count += 1
	x,y = move(x,y,heading)
#	printgrid(grid,x,y)

print('part 1: after {} bursts of activity, {} bursts cause a node to be infected'.format(n,count))


# Part 2

lines = [l.strip('\n') for l in open('day22_input.txt')]

# represent the infinite grid as a dictionary
grid = {}
for i in range(len(lines)): # rows
	for j in range(len(lines[i])): # cols
		grid[(i,j)] = lines[i][j] # so grid([x,y]) is horiz,vert


heading = 'N'	# N,S,E,W
x,y = 12,12		# starting position

count = 0 # keep track of number of infections
n = 10000000
for i in range(n):
	if (((x,y) in grid.keys()) == False):
		grid[(x,y)] = '.'
	if (grid[(x,y)] == '.'):
		heading = turnleft(heading)
		grid[(x,y)] = 'W'
	elif (grid[(x,y)] == 'W'):
		grid[(x,y)] = '#'
		count += 1
	elif (grid[(x,y)] == '#'):
		heading = turnright(heading)
		grid[(x,y)] = 'F'
	elif (grid[(x,y)] == 'F'):
		heading = turnreverse(heading)
		grid[(x,y)] = '.'

	x,y = move(x,y,heading)
#	printgrid(grid,x,y)

print('part 2: after {} bursts of activity, {} bursts cause a node to be infected'.format(n,count))







