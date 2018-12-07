# Advent of Code 2018 Day 7

# Solution from reddit.
# I couldn't stomach the nuisance factor for this one.
# Life interferes!

# Part One

import sys

lines = [l.split() for l in open("day07_input.txt")]
lines = [(l[1], l[7]) for l in lines]

steps = set([s[0] for s in lines] + [s[1] for s in lines])


def next_step(steps, l):
    return [s for s in steps if all(b != s for (_, b) in l)]


order = ''
while steps:
    cand = list(next_step(steps, lines))
    cand.sort()

    n = cand[0]
    order += n
    steps.remove(n)
    lines = [(a, b) for (a, b) in lines if a != n]

print(order)

# Part 2

from collections import defaultdict, deque
# Edges
E = defaultdict(list)
# In-degree
D = defaultdict(int)
for line in open('day07_input.txt'):
 words = line.split()
 x = words[1]
 y = words[7]
 E[x].append(y)
 D[y] += 1

for k in E:
 E[k] = sorted(E[k])

# time
t = 0
# Events
EV = []
# Work queue
Q = []
def add_task(x):
 Q.append(x)
def start_work():
 global Q
 while len(EV) < 5 and Q:
     x = min(Q)
     Q = [y for y in Q if y!=x]
     print('Starting {} at {}'.format(x, t))
     EV.append((t+61+ord(x)-ord('A'), x))

for k in E:
 if D[k] == 0:
     add_task(k)
start_work()

while EV or Q:
 t, x = min(EV)
 print(t,x)
 EV = [y for y in EV if y!=(t,x)]
 for y in E[x]:
     D[y] -= 1
     if D[y] == 0:
         add_task(y)
 start_work()

print(t)

