# Advent of Code Day 5 Part 1

f = open("day05_input.txt","r")
p = f.readline()
f.close()

n = len(p)
nprev = n+1
while (n < nprev):
	nprev = n
	for i in range(26): # for aA Aa to zZ Zz
		p = p.replace(chr(ord('A')+i) + chr(ord('a')+i) ,"") # disappear Aa
		p = p.replace(chr(ord('a')+i) + chr(ord('A')+i) ,"") # disappear aA
	n = len(p)
print("Day 5 Part 1: {:d} units remain".format(len(p)))


# Part 2

f = open("day05_input.txt","r")
p_orig = f.readline()
f.close()

min_len = len(p)
for ii in range(26): # for A/a to Z/z
	p = p_orig.replace(chr(ord('A')+ii), "").replace(chr(ord('a')+ii), "") # KGB the agitators
	n = len(p)
	nprev = n+1
	while (n < nprev):
		nprev = n
		for i in range(26): # for aA Aa to zZ Zz
			p = p.replace(chr(ord('A')+i) + chr(ord('a')+i) ,"") # disappear Aa
			p = p.replace(chr(ord('a')+i) + chr(ord('A')+i) ,"") # disappear aA
		n = len(p)
	if (n < min_len):
		min_len = n
print("Day 5 Part 2: {:d} units remain".format(min_len))




