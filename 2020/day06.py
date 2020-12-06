
groups = []  # for part 1
grp = set()

people = []     # for part 2
person = set()

s = ''

count1 = 0
count2 = 0
with open("day06_input.txt") as f:
	for line in f:
		if line=='\n':
			groups.append(grp)
			count1 += len(grp)
			count2 += len(set.intersection(*people))
			grp = set()
			s = ''
			people = []
		else:
			line = line.strip('\n')
			person = set()
			for i in range(len(line)):
				grp.add(line[i])
				s += line[i]
				person.add(line[i])
			people.append(person)
groups.append(grp)
count1 += len(grp)
count2 += len(set.intersection(*people))

print("Part 1: {}".format(count1))
print("Part 2: {}".format(count2))

