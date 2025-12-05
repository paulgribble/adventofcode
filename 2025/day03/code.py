with open("input") as f:
	BATT = [line.strip() for line in f.readlines()]

sum_voltage = 0
for B in BATT:
	max_voltage = 0
	l = len(B)
	for i1 in range(l):
		for i2 in range(i1,l):
			if (i1 != i2):
				max_voltage = max(max_voltage, int(B[i1]+B[i2]))
#	print(f"max_voltage: {max_voltage}")
	sum_voltage += max_voltage

print(f"part 1: {sum_voltage}")


sum_voltage = 0
for B in BATT:
	l = len(B)
	joltage = []
	i1,i2 = 0,l-12+1
	while (len(joltage)<12):
#		print(f"i1,i2: {i1},{i2}")
		imaxv = int(B[i1])
		imaxi = i1
		for i in range(i1,i2):
			if (int(B[i])>imaxv):
				imaxv = int(B[i])
				imaxi = i
		joltage.append(imaxv)
		i1=imaxi+1
		i2=i2+1
	sum_voltage += int("".join([str(x) for x in joltage]))

print(f"part 2: {sum_voltage}")

