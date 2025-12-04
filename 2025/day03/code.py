with open("input2") as f:
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

print(f"part 2: {sum_voltage}")

