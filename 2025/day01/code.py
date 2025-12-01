dial = 50
num_zero = 0
with open("input") as fid:
	for line in fid:
		if line[0]=='L':
			dial -= int(line[1:])
		elif line[0]=='R':
			dial += int(line[1:])
		dial = dial % 100
		if (dial==0):
			num_zero += 1
print(f"part 1: password = {num_zero}")

dial = 50
num_zero = 0
with open("input") as fid:
	for line in fid:
		if line[0]=='L':
			for r in range(int(line[1:])):
				dial -= 1
				if (dial<0):
					dial = dial + 100
				if (dial==0):
					num_zero += 1
		elif line[0]=='R':
			for r in range(int(line[1:])):
				dial += 1
				if (dial>99):
					dial = dial - 100
				if (dial==0):
					num_zero += 1
print(f"part 2: password = {num_zero}")



