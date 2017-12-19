

grid = [l.strip('\n') for l in open('day19_input.txt')]

x, y = 39, 0 # entry point into the grid

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
	tile = grid[y][x]
	if (tile == ' '):
		done = True
	else:
		if (tile=='+'):
			if (heading in ('S', 'N')):
				if (grid[y][x-1] != ' '):
					heading = 'W'
				else:
					heading = 'E'
			else:
				if (grid[y-1][x] != ' '):
					heading = 'N'
				else:
					heading = 'S'

		elif (tile not in ('|', '-')):
			letters.append(tile)

print('part 1: we will see the letters {}'.format(''.join(letters)))
print('part 2: we will take {} steps'.format(steps))
