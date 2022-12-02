# PART 1
#
score = 0
points2 = {'X'  :1, 'Y'  :2, 'Z'  :3}
points12= {'A X':3, 'A Y':6, 'A Z':0, \
           'B X':0, 'B Y':3, 'B Z':6, \
           'C X':6, 'C Y':0, 'C Z':3}
with open("day02_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        score = score + points2[line[2]] + points12[line]
print(f"Part 1: score is {score}")


# PART 2
#
score = 0
points1 = {'X'  :1, 'Y'  :2, 'Z'  :3}
points2 = {'X'  :0, 'Y'  :3, 'Z'  :6}
points12= {'A X':'Z', 'A Y':'X', 'A Z':'Y', \
           'B X':'X', 'B Y':'Y', 'B Z':'Z', \
           'C X':'Y', 'C Y':'Z', 'C Z':'X'}
with open("day02_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        score = score + points1[points12[line]] + points2[line[2]]
print(f"Part 2: score is {score}")


