# PART 1
#
count = 0
with open("day04_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        s1,s2 = line.split(',')
        s1,s2 = s1.split('-'), s2.split('-')
        s1i,s2i = [int(s) for s in s1], [int(s) for s in s2]
        if ( ((s2i[0]>=s1i[0]) and (s2i[1]<=s1i[1])) or \
             ((s1i[0]>=s2i[0]) and (s1i[1]<=s2i[1])) ):
            count = count + 1
print(f"Part 1: answer is {count}")

# PART 2
#
count = 0
with open("day04_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        s1,s2 = line.split(',')
        s1,s2 = s1.split('-'), s2.split('-')
        s1i,s2i = [int(s) for s in s1], [int(s) for s in s2]
        s1is = set(list(range(s1i[0],s1i[1]+1)))
        s2is = set(list(range(s2i[0],s2i[1]+1)))
        if (len(s1is.intersection(s2is)) > 0):
            count = count + 1
print(f"Part 2: answer is {count}")

