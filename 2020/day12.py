with open("day12_input.txt") as f:
	A = [l.strip('\n') for l in f]

steps = ((1,0),(0,1),(-1,0),(0,-1)) # E,N,W,S

sx,sy,sd = 0,0,0 # ship starting position 0,0 (grid pos) and direction (index into steps)

for a in A:
	action = a[0]
	value = int(a[1:])
	if action=='F':
		sx += steps[sd][0]*value
		sy += steps[sd][1]*value
	elif action=='R':
		sd = (sd - int(value/90)) % 4
	elif action=='L':
		sd = (sd + int(value/90)) % 4
	elif action=='W':
		sx -= value
	elif action=='E':
		sx += value
	elif action=='S':
		sy -= value
	elif action=='N':
		sy += value

print("Part 1: {}".format(abs(sx)+abs(sy)))


sx,sy,sd = 0,0,0 # starting position 0,0 (grid pos) and index into compass direction 0 ('E')
wx,wy = 10,1     # waypoint position _relative to ship_

for a in A:
	action = a[0]
	value = int(a[1:])
	if action=='F':
		sx += wx*value
		sy += wy*value
	elif ((action,value)==('L',180)) or ((action,value)==('R',180)):
			wx,wy = -wx,-wy
	elif ((action,value)==('L',90)) or ((action,value)==('R',270)):
			wx,wy = -wy,wx
	elif ((action,value)==('L',270)) or ((action,value)==('R',90)):
			wx,wy = wy,-wx			
	elif action=='W':
		wx -= value
	elif action=='E':
		wx += value
	elif action=='S':
		wy -= value
	elif action=='N':
		wy += value

print("Part 1: {}".format(abs(sx)+abs(sy)))

