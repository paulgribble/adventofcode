with open("day09_input.txt") as f:
	code = [int(r.strip('\n')) for r in f]

def test(code, i, prev):
	n1,n2 = i-prev,i-prev
	valid = False
	while (not valid) and (n1<i):
		n2 = i-prev
		while (not valid) and (n2<i):
#			print("{},{},{},{},{}".format(i,n1,n2,code[n1]+code[n2]==code[i],n1!=n2))
			if (code[n1]+code[n2]==code[i]) and (n1!=n2):
				valid = True
			else:
				n2 += 1
		if (not valid):
			n1 +=1
	return valid,i,n1,n2

i = 25
prev = 25
valid = True
while valid:
	valid,ii,n1,n2 = test(code, i, prev)
	if valid:
		i += 1

print("Part 1: {}".format(code[i]))


