# Advent of Code 2018 Day 3

import numpy as np
import re

# Part 1

nn = 1280
fabric = np.zeros(shape=(nn,nn))

f = open("day03_input.txt","r")
for line in f:
#	ID,ll = line.strip('\n').split(" @ ")
#	corner, size = ll.split(": ")
#	cc,cr = corner.split(",")
#	sc,sr = size.split("x")
#	cc,cr,sc,sr = int(cc),int(cr),int(sc),int(sr)
	ID,cc,cr,sc,sr = map(int, re.findall(r'\d+', line))
	fabric[cr:cr+sr,cc:cc+sc] += 1
f.close()
num = sum(sum(fabric>=2))
print("Day 3 Part 1: {:d} sq inches of fabric are within two or more claims".format(num))

# Part 2
f = open("day03_input.txt","r")
for line in f:
#	ID,ll = line.strip('\n').split(" @ ")
#	corner, size = ll.split(": ")
#	cc,cr = corner.split(",")
#	sc,sr = size.split("x")
#	cc,cr,sc,sr = int(cc),int(cr),int(sc),int(sr)
#	fabric[cr:cr+sr,cc:cc+sc] += 1
	ID,cc,cr,sc,sr = map(int, re.findall(r'\d+', line))
	patch = fabric[cr:cr+sr,cc:cc+sc]
	if sum(sum(patch != 1)) == 0:
		print("Day 3 Part 2: {:d} is the ID of the claim that doesn't overlap".format(ID))
f.close()

