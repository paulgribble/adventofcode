with open("day19_input_test2.txt") as f:
	inp = [r.strip('\n') for r in f]

rules = {}

for l in inp:
	k,tmp = l.split(': ')
	k = int(k)
	if tmp[0] == '"':
		rules[k] = tmp.replace('"','')
	else:
		if tmp.find(' | ')==-1:
			rules[k] = list(map(int,tmp.split(' ')))
		else:
			v1,v2 = tmp.split(' | ')
			rules[k] = [list(map(int,v1.split(' '))), list(map(int,v2.split(' ')))]



