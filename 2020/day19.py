with open("day19_input_test.txt") as f:
	inp = [r.strip('\n') for r in f]

rules = {}

for l in inp:
	k,tmp = l.split(': ')
	k = int(k)
	if tmp[0] == '"':
		rules[k] = tmp.replace('"','')
	else:
		if tmp.find(' | ')==-1:
			rules[k] = tmp
		else:
			v1,v2 = tmp.split(' | ')
			rules[k] = [v1,v2]

