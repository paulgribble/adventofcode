with open("day08_input.txt") as f:
	code = [r.strip('\n') for r in f]


def is_inf_loop(code):
	flags = [False]*len(code)
	A,i = 0,0
	halt = False
	while i<len(code) and flags[i]==False:
		flags[i] = True
		sign = 1 if code[i][4]=='+' else -1
		if code[i][0:3]=='nop':
			i += 1
		elif code[i][0:3]=='jmp':
			i += sign*int(code[i][5:])
		elif code[i][0:3]=='acc':
			A += sign*int(code[i][5:])
			i += 1
	inf = True if i<len(code) else False
	return inf, A

inf,A = is_inf_loop(code)
print("Part 1: {}".format(A))


iswitch = 0
found = False
while not found:
	codenew = code.copy()
	if codenew[iswitch][0:3]=='nop':
		codenew[iswitch] = codenew[iswitch].replace('nop','jmp')
	elif codenew[iswitch][0:3]=='jmp':
		codenew[iswitch] = codenew[iswitch].replace('jmp','nop')
	inf,A = is_inf_loop(codenew)
	found = False if inf else True
	iswitch +=1

print("Part 2: {}".format(A))
