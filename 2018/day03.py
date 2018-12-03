# Advent of Code 2018 Day 3

import numpy as np 

nn = 1280
fabric = np.zeros(shape=(nn,nn))
f = open("day03_input.txt","r")
for line in f:
	n,ll = line.strip('\n').split(" @ ")
	corner, size = ll.split(": ")
	cc,cr = corner.split(",")
	sc,sr = size.split("x")
	cc,cr,sc,sr = int(cc),int(cr),int(sc),int(sr)
	fabric[cr:cr+sr,cc:cc+sc] += 1
f.close()
num = sum(sum(fabric>=2))
print("Day 3 Part 1: {:d} sq inches of fabric are within two or more claims".format(num))

