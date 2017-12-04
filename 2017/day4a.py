

lines = [line.rstrip('\n') for line in open('day4_input.txt')]

count = 0;
for l in lines:
	s = l.split()
	ss = set(s)	# builds an unordered collection of UNIQUE elements
	if len(s)==len(ss):
		count = count + 1
print(count)


