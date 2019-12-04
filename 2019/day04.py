
def passes1(x):
	s = str(x)
	inc = True
	rep = False
	for i in range(1,len(s)):
		if (s[i] < s[i-1]):
			inc = False
			break
		if (s[i-1] == s[i]):
			rep = True
	return (inc and rep)

def passes2(x):
	s = str(x)
	inc = True
	rep = False
	for i in range(1,len(s)):
		if (s[i] < s[i-1]):
			inc = False
			break
		if (s[i-1] == s[i]):
			multiple = False
			for j in range(i-1):
				if (s[j]==s[i]):
					multiple = True
					break
			if (multiple==False):
				for j in range(i+1, len(s)):
					if (s[j]==s[i]):
						multiple = True
						break
			if (multiple==False):
				rep = True
	return (inc and rep)

min = 265275
max = 781584
count1 = 0
count2 = 0
for i in range(min,max+1):
	count1 = count1 + passes1(i)
	count2 = count2 + passes2(i)
print("Part 1: answer is {:d}".format(count1))
print("Part 2: answer is {:d}".format(count2))

