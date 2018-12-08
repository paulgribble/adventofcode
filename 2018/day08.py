# Advent of Code 2018 Day 8

# Solution adapted from reddit user sciyoshi
# darn recursion!

f = open("day08_input.txt")
data = f.readline().split()
data = list(map(int, data))
f.close()

def process(data):
    nchild, nmeta = data[0], data[1]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(nchild):
        total, score, data = process(data)
        totals += total
        scores.append(score)

    totals += sum(data[:nmeta])

    if nchild == 0:
        return (totals, sum(data[:nmeta]), data[nmeta:])
    else:
        return (
            totals,
            sum(scores[k-1] for k in data[:nmeta] if k > 0 and k <= len(scores)),
            data[nmeta:]
        )

total, value, remaining = process(data)

print('part 1:', total)
print('part 2:', value)

