
import math

lines = [line.strip('\n') for line in open("day11_input.txt")]
path = lines[0].split(',')

# cube space, see https://www.redblobgames.com/grids/hexagons/
x, y, z = 0, 0, 0
maxdist = 0
for step in path:
	if (step=='ne'):
		x += 1
		y += 0
		z -= 1
	elif (step=='n'):
		x += 0
		y += 1
		z -= 1
	elif (step=='nw'):
		x -= 1
		y += 1
		z += 0
	elif (step=='sw'):
		x -= 1
		y += 0
		z += 1
	elif (step=='s'):
		x += 0
		y -= 1
		z += 1
	elif (step=='se'):
		x += 1
		y -= 1
		z += 0
	distance = (abs(x) + abs(y) + abs(z)) / 2
	if (distance > maxdist):
		maxdist = distance

print('steps to reach him is {}'.format(distance))
print('furthest to reach him was {}'.format(maxdist))
