

lines = [line.rstrip('\n') for line in open('day4_input.txt')]

count = 0;
for l in lines:
	s = l.split(' ')
	snew = []
	# sort all strings
	for ss in s:
		tmp = sorted(ss)
		ss = ''.join(tmp)
		snew.append(ss)
	ss = set(snew)	# builds an unordered collection of UNIQUE elements
	if len(snew)==len(ss):
		count = count + 1
print(count)


