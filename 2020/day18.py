with open("day18_input.txt") as f:
	inp = [r.strip('\n') for r in f]

e = "1 + (2 * 3) + (4 * (5 + 6))"


def parse(e):
	print('e: {}'.format(e))
	if e=='':
		print('empty: 0')
		return 0
	elif e.find(' ')==-1:
		print('no space: {}'.format(int(e)))
		return int(e)
	elif e[0] in '0123456789':
		i = e.find(' ')
		val1 = int(e[:i])
		print('val1: {}'.format(val1))
	elif e[0]=='(':
		depth = 1
		i = 1
		while depth>0 and i<len(e[1:]):
			if e[i]=='(':
				depth += 1
			elif e[i]==')':
				depth -= 1
			i += 1
		val1 = parse(e[:i])
		print('(: val1: {}'.format(val1))
	op = e[i+1]
	val2 = parse(e[i+3:])
	if op=='+':
		return val1 + val2
	elif op=='-':
		return val1 - val2
	elif op=='*':
		return val1 * val2
	elif op=='/':
		return val1 / val2




