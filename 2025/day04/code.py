with open("input") as f:
        ROLLS = [list(line.strip()) for line in f.readlines()]

dir_list = [[0,-1], [1,-1], [1, 0], [1, 1],
            [0, 1], [-1,1], [-1,0], [-1,-1]]

roll_count = 0
rows = len(ROLLS)
cols = len(ROLLS[0])
for i in range(rows):
	for j in range(cols):
		if (ROLLS[i][j]=='@'):
			paper_count = 0
			for k in range(8):
				if ((i+dir_list[k][0])>=0 and (i+dir_list[k][0])<rows and
				   (j+dir_list[k][1])>=0 and (j+dir_list[k][1])<cols) :
#					print(f"{i},{j} : {i+dir_list[k][0]},{j+dir_list[k][1]} : {ROLLS[i+dir_list[k][0]][j+dir_list[k][1]]}")
					if (ROLLS[i+dir_list[k][0]][j+dir_list[k][1]]=='@'):
						paper_count += 1
#			print(paper_count)
			if (paper_count < 4):
				roll_count += 1

print(f"part 1: {roll_count}")


def remove_rolls(ROLLS):
	roll_count = 0
	rows = len(ROLLS)
	cols = len(ROLLS[0])
	remove_list = []
	for i in range(rows):
		for j in range(cols):
			if (ROLLS[i][j]=='@'):
				paper_count = 0
				for k in range(8):
					if ((i+dir_list[k][0])>=0 and (i+dir_list[k][0])<rows and
					   (j+dir_list[k][1])>=0 and (j+dir_list[k][1])<cols) :
						# print(f"{i},{j} : {i+dir_list[k][0]},{j+dir_list[k][1]} : {ROLLS[i+dir_list[k][0]][j+dir_list[k][1]]}")
						if (ROLLS[i+dir_list[k][0]][j+dir_list[k][1]]=='@'):
							paper_count += 1
				# print(paper_count)
				if (paper_count < 4):
					roll_count += 1
					remove_list.append([i,j])
	for ij in remove_list:
		ROLLS[ij[0]][ij[1]] = '.'
	return ROLLS, roll_count

ROLLS,roll_count = remove_rolls(ROLLS)
roll_total = roll_count
while (roll_count > 0):
	ROLLS,roll_count = remove_rolls(ROLLS)
	roll_total += roll_count

print(f"part 2: {roll_total}")
