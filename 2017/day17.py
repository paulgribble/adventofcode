

# Part 1

S = [0]
Slen = 1
pos = 0
step = 366
for v in range(2017):
#	print('{}'.format(S))
	pos = (pos + step) % Slen
	S.insert(pos+1, v+1)
	Slen += 1
	pos = (pos + 1) % Slen

print('part 1: the value after 2017 is {}'.format(S[pos+1]))


# Part 2

from collections import deque

step = 366
S = deque([0])
for i in range(1, 50000001):
	if ((i % 1000000)==0):
		print('{} mil'.format(int(i/1000000)))
	S.rotate(step)
	S.insert(0, i)

print('part 2: the value after 0 is {}'.format(S[S.index(0) - 1]))


