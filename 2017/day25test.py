
from collections import defaultdict

tape = defaultdict(int)
pos = 0
positions = set()
n = 6
state = 'A'
for i in range(n):
    positions.add(pos)
    if (state=='A'):
        if (tape[pos]):
            tape[pos] = 0
            pos -= 1
            state = 'B'
        else:
            tape[pos] = 1
            pos += 1
            state = 'B'
    elif (state=='B'):
        if (tape[pos]):
            tape[pos] = 1
            pos += 1
            state = 'A'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'A'

count = 0
for p in positions:
    if (tape[p]):
        count += 1

print('count = {}'.format(count))

