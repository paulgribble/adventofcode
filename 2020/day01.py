import numpy as np

E = np.loadtxt("day01_input.txt", dtype='int')
n = np.shape(E)[0]
done = False

i = 0
while ((~ done) & (i<n)):
	j = 0
	while ((~ done) & (j<n)):
		if ((E[i]+E[j])==2020):
			print("Part 1: {:d}*{:d}={:d}".format(E[i],E[j],E[i]*E[j]))
			done = True
		j = j + 1
	i = i + 1

done = False
i = 0
while ((~ done) & (i<n)):
	j = 0
	while ((~ done) & (j<n)):
		k = 0
		while ((~done) & (k<n)):
			if ((E[i]+E[j]+E[k])==2020):
				print("Part 2: {:d}*{:d}*{:d}={:d}".format(E[i],E[j],E[k],E[i]*E[j]*E[k]))
				done = True
			k = k + 1
		j = j + 1
	i = i + 1



