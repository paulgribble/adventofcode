with open("day01_input.txt") as f:
	E = [int(x) for x in f]

n = len(E)

done = False
i = 0
while (not done and i<n):
	j = 0
	while (not done and j<n):
		if ((E[i]+E[j])==2020):
			print("Part 1: {:d}".format(E[i]*E[j]))
			done = True
		j = j + 1
	i = i + 1

done = False
i = 0
while (not done and i<n):
	j = 0
	while (not done and j<n):
		k = 0
		while (not done and k<n):
			if ((E[i]+E[j]+E[k])==2020):
				print("Part 2: {:d}".format(E[i]*E[j]*E[k]))
				done = True
			k = k + 1
		j = j + 1
	i = i + 1

