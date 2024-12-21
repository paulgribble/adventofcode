

with open("day11_input.txt") as f:
    S = f.read().split(' ')

def blink(S):
    n = len(S)
    S2 = S.copy()
    i = 0
    while i < len(S2):
        if S2[i]=='0':
            x = '1'
            #print(f"{i}: {S2[i]} -> {x}")
            S2[i] = x
            i += 1
        elif (len(S2[i])%2)==0:
            pivot = int(len(S2[i])/2)
            x = [S2[i][0:pivot], S2[i][pivot:]]
            #print(f"{i}: {S2[i]} -> {x}")
            S2.insert(i, str(int(x[0])))
            S2[i+1] = str(int(x[1]))
            i += 2
        else:
            x = str(int(S2[i])*2024)
            #print(f"{i}: {S2[i]} -> {x}")
            S2[i] = x
            i += 1
    return S2
    
for i in range(25):
    S = blink(S)

print(f"Part 1: {len(S)}")

# Part 2

def update_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[:len(stone)//2]), int(stone[len(stone)//2:])]
    else:
        return [stone * 2024]

def update(arrangement):
    new_arrangement = {}
    for stone in arrangement.keys():
        new_stones = update_stone(stone)
        for new_stone in new_stones:
            if new_stone not in new_arrangement.keys():
                new_arrangement[new_stone] = 0
            new_arrangement[new_stone] += arrangement[stone]
    return new_arrangement


with open("day11_input.txt") as f:
    arrangement = {i: 1 for i in map(int, f.read().split())}

for _ in range(75):
    arrangement = update(arrangement)

print(f"Part 2: {sum(arrangement.values())}")
