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



# part 2 with help from reddit

datafile = open('input', "r", encoding="UTF-8").read().strip().splitlines()
empty_line = datafile.index("")
s_ranges = datafile[:empty_line]

def parse_range(rng):
    a, b = map(int, rng.split('-'))
    return a, b

ranges = sorted(parse_range(r) for r in s_ranges)

def merge_ranges(a,b):
    start = min(a[0], b[0])
    end = max(a[1], b[1])
    return start, end

def overlaps(a,b):
    return (b[1] >= a[0] and b[0] <= a[1])

final = []
current = ranges[0]
for range in ranges[1:]:
    if overlaps(current, range):
        current = merge_ranges(current, range)
    else:
        final.append(current)
        current = range
final.append(current)

fresh = sum([b-a+1 for a, b in final])

print(f"part 2: {fresh}")



