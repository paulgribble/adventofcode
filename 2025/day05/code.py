range_list = []
ids = []
with open("input") as f:
        isRanges = True
        for line in f:
                line = line.strip()
                if (line==""):
                        isRanges = False
                else:
                        if isRanges:
                                r = line.split('-')
                                range_list.append([int(r[0]), int(r[1])])
                        else:
                                ids.append(int(line))

num_fresh = 0
for i in ids:
        isFresh = False
        for j in range_list:
                if ((i>=j[0]) and (i<=j[1])):
                        isFresh = True
                        num_fresh += 1
                        break

print(f"part 1: {num_fresh}")

