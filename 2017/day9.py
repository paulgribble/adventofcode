

lines = [line.strip('\n') for line in open("day9_input.txt")]
stream = lines[0]

#stream = "{{{},{},{{}}}}"
#stream = "{{},{}}"
#stream = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
#stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
#stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#stream = "<random characters>"
#stream = "<{o'i!a,<{i<a>"

depth = 0
score = 0
garbagechars = 0
garbage = False
skip = False
for c in stream:
	if (skip == False):
		if (c=='!'):
			skip = True
		else:
			if (garbage == False):
				if (c=='{'):
					depth += 1
					score += depth
				elif (c=='}'):
					depth -= 1
				elif (c=='<'):
					garbage = True
			else:
				if (c=='>'):
					garbage = False
				else:
					garbagechars += 1
	else:
		skip = False

print(depth)
print(score)
print(garbagechars)

