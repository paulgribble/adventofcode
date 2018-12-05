# Advent of Code Day 5 Part 1

f = open("day05_input.txt","r")
p = f.readline()
f.close()

n = len(p)
nprev = n+1
while (n < nprev):
	nprev = n
	for i in range(26): # for aA Aa to zZ Zz
		p = p.replace(chr(ord('A')+i)+chr(ord('a')+i) ,"") # Aa
		p = p.replace(chr(ord('a')+i)+chr(ord('A')+i) ,"") # aA
	n = len(p)

# Part 2


