
import numpy as np

lines = [l.strip('\n') for l in open('day20_input.txt')]
ll = len(lines)
pos = np.zeros((ll,3))
vel = np.zeros((ll,3))
acc = np.zeros((ll,3))

# Part 1

for i in range(ll):
	p,v,a=lines[i].split(', ')
	pos[i] = list(map(int,p.strip('p=<,>').split(',')))
	vel[i] = list(map(int,v.strip('v=<,>').split(',')))
	acc[i] = list(map(int,a.strip('a=<,>').split(',')))

n = 10000
for i in range(n):
	vel += acc
	pos += vel
	p0 = sum(abs(pos.T)).argmin()

print('part 1: after {} ticks particle {} is closest to zero'.format(i,p0))

# Part 2

from collections import defaultdict

lines = [l.strip('\n') for l in open('day20_input.txt')]
ll = len(lines)
pos = {}
vel = {}
acc = {}
for i in range(ll):
	p,v,a=lines[i].split(', ')
	pos[i] = list(map(int,p.strip('p=<,>').split(',')))
	vel[i] = list(map(int,v.strip('v=<,>').split(',')))
	acc[i] = list(map(int,a.strip('a=<,>').split(',')))

n = 100
for _ in range(n):
	for i,p in pos.items():
		vel[i] = [vel[i][0]+acc[i][0], vel[i][1]+acc[i][1], vel[i][2]+acc[i][2]]
		pos[i] = [pos[i][0]+vel[i][0], pos[i][1]+vel[i][1], pos[i][2]+vel[i][2]]
	pdict = defaultdict(list)
	for i,p in pos.items():
		k = tuple(p)
		pdict[k].append(i)
	for k, v in pdict.items():
		if len(v) > 1:
#			print('{} has {} reps'.format(k,len(v)))
#			print('deleting {}'.format(len(v)))
			for i in v:
				del pos[i]
				del vel[i]
				del acc[i]

print('part 2: {} particles are left after all collisions are resolved'.format(len(pos)))




