with open("day18_input.txt") as f:
	inp = [r.strip('\n') for r in f]

def mathme(val1,op,val2):
	val1,val2 = int(val1), int(val2)
	if op=='+':
		return val1 + val2
	elif op=='*':
		return val1 * val2

def parse(e):
	if e.find(' ')==-1: # must be a single integer
		return int(e)
	elif e[0] in '0123456789': # more than one term is left
		i = e.find(' ')
		val1 = int(e[:i])
		op = e[i+1]
		val2 = parse(e[i+3:])
		r = mathme(val1,op,val2)
		return r
	elif e[0]=='(':
		depth = 1
		i = 1
		while depth>0 and i<len(e):
			if e[i]=='(':
				depth += 1
			elif e[i]==')':
				depth -= 1
			i += 1
		i -= 1
		if i == len(e)-1:
			return parse(e[1:i])
		else:
			val1 = parse(e[1:i])
			op = e[i+2]
			val2 = parse(e[i+4:])
			return mathme(val1, op, val2)

p1 = 0
for e in inp:
	er = e.replace('(','$').replace(')','(').replace('$',')')[::-1] # reverse it
	p1 += parse(er)

print("Part 1: {}".format(p1))


def rebracket(e):
	
	return e

p2 = 0
for e in inp:
	eb = rebracket(e)
	er = eb.replace('(','$').replace(')','(').replace('$',')')[::-1]
	p2 += parse(er)

print("Part 2: {}".format(p2))


