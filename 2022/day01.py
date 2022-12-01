# PART 1
maxcal = 0
ecal = 0
with open("day01_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
#        print(f'{line:5s} | {ecal:7d} | {maxcal:7d}')
        if (len(line)==0):
            maxcal = max(maxcal, ecal)
            ecal = 0
        else:
            ecal = ecal + int(line)

print(f'Part 1: max is {maxcal}')

# PART 2
top3 = [0,0,0]
ecal = 0
with open("day01_input.txt", 'r') as file:
    for line in file:
        line = line.strip()
#        print(f'{line:5s} | {ecal:7d} | {maxcal:7d}')
        if (len(line)==0):
            if (ecal > top3[0]):
                top3[2] = top3[1]
                top3[1] = top3[0]
                top3[0] = ecal
            elif (ecal > top3[1]):
                top3[2] = top3[1]
                top3[1] = ecal
            elif (ecal > top3[2]):
                top3[2] = ecal
            ecal = 0
        else:
            ecal = ecal + int(line)

print(f'Part 2: total top 3 is {sum(top3)}')

