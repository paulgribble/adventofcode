from itertools import combinations

with open("day07_input.txt") as f:
    data = [line.strip() for line in f.readlines()]

n = len(data)

def is_valid(v,e):
    if len(e)==1:
        return v == e[0]
    if is_valid(v, [e[0]+e[1]] + e[2:]):
        return True
    if is_valid(v, [e[0]*e[1]] + e[2:]):
        return True
    return False

count = 0
for eq in data:
    v,e = eq.split(': ')
    v = int(v)
    ei = [int(x) for x in e.split(' ')]
    if is_valid(v,ei):
        count += v
print(f"Part 1: {count}")

def is_valid2(v,e):
    if len(e)==1:
        return v == e[0]
    if is_valid2(v, [e[0]+e[1]] + e[2:]):
        return True
    if is_valid2(v, [e[0]*e[1]] + e[2:]):
        return True
    if is_valid2(v, [int(str(e[0]) + str(e[1]))] + e[2:]):
        return True
    return False

count = 0
for eq in data:
    v,e = eq.split(': ')
    v = int(v)
    ei = [int(x) for x in e.split(' ')]
    if is_valid2(v,ei):
        count += v
print(f"Part 2: {count}")
