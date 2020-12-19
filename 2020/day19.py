with open("day19_input_test2.txt") as f:
	inp = [r.strip('\n') for r in f]

rules = {}
messages = []






readrules = True
for l in inp:
	if l=='' and readrules:
		readrules = False
	if readrules:
		v,k = l.split(': ')
		if k[0] == '"':
			if k[1]=='a':
				a_r = v
			elif k[1]=='b':
				b_r = v
		elif l.find(' | ')==-1:
			k = k.replace(' ','')
			rules[k] = v
		else:
			a,b = k.split(' | ')
			a,b = a.replace(' ',''), b.replace(' ','')
			rules[a] = v
			rules[b] = v
	else:
		if l != '':
			messages.append(l)


mi = messages[0]
m = mi.replace('a',a_r).replace('b',b_r)

def valid(m):



