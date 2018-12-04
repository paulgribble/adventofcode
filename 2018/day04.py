# Advent of Code 2018 Day 4

import numpy as np

records = [line.strip('\n') for line in open("day04_input.txt","r")]
records.sort()

G = dict() # each guard has an array of 60 minutes

for r in records:
	r = r.replace('[',' ').replace(']',' ').replace(':',' ').replace('#',' ').split()
	if r[3]=='Guard':
		guard = int(r[4])
		if guard not in G:
			G[guard] = np.zeros(shape=(60))
	elif r[3]=='falls':
		time1 = int(r[2])
	elif r[3]=='wakes':
		time2 = int(r[2])
		G[guard][time1:time2] += 1

sleepy_guard = 0
most_sleep = 0
for k in G.keys():
	if sum(G[k]) > most_sleep:
		most_sleep = sum(G[k])
		sleepy_guard = k
sleepy_minute = np.argmax(G[sleepy_guard])

print("Day 4 Part 1: ID of guard x minute = {:d}".format(sleepy_guard * sleepy_minute))

# Part 2

most_sleep = 0
sleepy_minute = 0
sleepy_guard = 0
for k in G.keys():
	if np.max(G[k]) > most_sleep:
		most_sleep = np.max(G[k])
		sleepy_minute = np.argmax(G[k])
		sleepy_guard = k

print("Day 4 Part 2: ID of guard x minute = {:d}".format(sleepy_guard * sleepy_minute))

	

