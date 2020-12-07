with open("day07_input.txt") as f:
	rule_list= [r.strip('\n') for r in f]

# use a dictionary of dictionaries
rules = {}
for i in range(len(rule_list)):
	outer = rule_list[i].split(' contain ')[0][:-5]
	tmp = rule_list[i].split(' contain ')[1]
	tmp = tmp.strip('.').replace(' bags','').replace(' bag','')
	tmp = tmp.split(', ')
	r = {}
	for t in tmp:
		if tmp != ['no other']:
			r[t[2:]] = int(t[:2]) # assumes only single digits
		rules[outer] = r

def csg(c): # contains shiny gold
	if c=='shiny gold':
		return True
	else:
		for cc in rules[c]:
			if csg(cc):
				return True
	return False

count = 0
for c in rules.keys():
	if c!='shiny gold' and csg(c):
		count += 1

print("Part 1: {}".format(count))

def countbags(c):
	if rules[c]=={}:
		return 1
	else:
		if c=='shiny gold':
			count = 0
		else:
			count = 1
		for k in rules[c]:
			count += rules[c][k]*countbags(k)
		return count

count = countbags('shiny gold')

print("Part 2: {}".format(count))

