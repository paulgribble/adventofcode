

grid = [l.strip('\n') for l in open('day19_input.txt')]

x,y = 39,0 # entry point into the grid

heading = 'S'
letters = []
tile = '|'
steps = 0
done = False
while (done==False):
	steps += 1
	if (heading=='S'):
		y += 1
	elif (heading=='N'):
		y -= 1
	elif (heading=='W'):
		x -= 1
	elif (heading=='E'):
		x += 1
	tile = grid[y][x] # be careful: y (north/south) is rows, x is cols
	if (tile == ' '): # we're done
		done = True
	elif (tile in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
		letters += tile # add letter and keep on same heading
	elif (tile=='+'):
		if ((heading=='N') | (heading=='S')):
			look_west = grid[y][x-1]
			if (look_west==' '): # don't go that way
				heading = 'E'
			else:
				heading = 'W'
		else: # heading is E or W
			look_north = grid[y-1][x]
			if (look_north==' '): # don't go that way
				heading = 'S'
			else:
				heading = 'N'

print('part 1: we will see the letters {}'.format(''.join(letters)))
print('part 2: we will take {} steps'.format(steps))
