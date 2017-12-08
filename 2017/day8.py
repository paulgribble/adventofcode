# part 1

lines = [line.strip('\n') for line in open("day8_input.txt")]

registers = {} # use a dictionary to store register names and their values

for line in lines:
	instruction, condition = line.split('if ')
	r1,c,v1 = condition.split()
	r2,op,v2 = instruction.split()
	if ((r1 in registers)==False):
		registers[r1] = 0
	if ((r2 in registers)==False):
		registers[r2] = 0
	test = "registers['" + r1 + "']" + c + v1
	if (eval(test)):
		if (op == 'inc'):
			registers[r2] = registers[r2] + int(v2)
		elif (op =='dec'):
			registers[r2] = registers[r2] - int(v2)

max = 0
for key in registers:
	if (registers[key] > max):
		max = registers[key]
print(max)

# part 2

lines = [line.strip('\n') for line in open("day8_input.txt")]

registers = {} # use a dictionary to store register names and their values

maxmax = 0
for line in lines:
	instruction, condition = line.split('if ')
	r1,c,v1 = condition.split()
	r2,op,v2 = instruction.split()
	if ((r1 in registers)==False):
		registers[r1] = 0
	if ((r2 in registers)==False):
		registers[r2] = 0
	test = "registers['" + r1 + "']" + c + v1
	if (eval(test)):
		if (op == 'inc'):
			registers[r2] = registers[r2] + int(v2)
		elif (op =='dec'):
			registers[r2] = registers[r2] - int(v2)
	max = 0
	for key in registers:
		if (registers[key] > max):
			max = registers[key]
	if (max > maxmax):
		maxmax = max

print(maxmax)


