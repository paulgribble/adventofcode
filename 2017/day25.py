
from collections import defaultdict

tape = defaultdict(int)
pos = 0
positions = set()
n = 12667664
state = 'A'
for i in range(n):
    positions.add(pos)
    if (state=='A'):
        if (tape[pos]):
            tape[pos] = 0
            pos -= 1
            state = 'C'
        else:
            tape[pos] = 1
            pos += 1
            state = 'B'
    elif (state=='B'):
        if (tape[pos]):
            tape[pos] = 1
            pos += 1
            state = 'D'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'A'
    elif (state=='C'):
        if (tape[pos]):
            tape[pos] = 0
            pos -= 1
            state = 'E'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'B'
    elif (state=='D'):
        if (tape[pos]):
            tape[pos] = 0
            pos += 1
            state = 'B'
        else:
            tape[pos] = 1
            pos += 1
            state = 'A'
    elif (state=='E'):
        if (tape[pos]):
            tape[pos] = 1
            pos -= 1
            state = 'C'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'F'
    elif (state=='F'):
        if (tape[pos]):
            tape[pos] = 1
            pos += 1
            state = 'A'
        else:
            tape[pos] = 1
            pos += 1
            state = 'D'

count = 0
for p in positions:
    if (tape[p]):
        count += 1

print('count = {}'.format(count))

