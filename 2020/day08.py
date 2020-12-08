with open("day08_input.txt") as f:
	code = [r.strip('\n') for r in f]

flags = [False]*len(code)
A,i = 0,0
halt = False
while flags[i]==False:
	flags[i] = True
	sign = 1 if code[i][4]=='+' else -1
	if code[i][0:3]=='nop':
		i += 1
	elif code[i][0:3]=='jmp':
		i += sign*int(code[i][5:])
	elif code[i][0:3]=='acc':
		A += sign*int(code[i][5:])
		i += 1

print("Part 1: {}".format(A))

iswitch = 0
while(flags[len(code)-1]==False):
	codenew = code.copy()
	if codenew[iswitch][0:3]=='nop':
		codenew[iswitch] = codenew[iswitch].replace('nop','jmp')
	elif codenew[iswitch][0:3]=='jmp':
		codenew[iswitch] = codenew[iswitch].replace('jmp','nop')
#	print(codenew)
	flags = [False]*len(codenew)
	A,i = 0,0
	halt = False
	while i<len(codenew) and flags[i]==False:
#		print("{},{}\r".format(i,iswitch))
		flags[i] = True
		sign = 1 if codenew[i][4]=='+' else -1
		if codenew[i][0:3]=='nop':
			i += 1
		elif codenew[i][0:3]=='jmp':
			i += sign*int(codenew[i][5:])
		elif codenew[i][0:3]=='acc':
			A += sign*int(codenew[i][5:])
			i += 1
	iswitch += 1

print("Part 2: {}".format(A))
