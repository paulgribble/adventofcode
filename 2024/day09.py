with open("day09_input.txt") as f:
    D = [int(x) for x in f.read()]

D2 = []
n_pos = {}
n = 0
for x in range(len(D)):
    if ((x%2)==0):
        if (D[x]>0):
            n_pos[n] = len(D2)
        for i in range(D[x]):
            D2.append(n)
        n += 1
    else:
        for i in range(D[x]):
            D2.append('.')

# Part 1
n = len(D2)-1
Dp1 = D2.copy()
for i in range(n,0,-1):
    if (Dp1[i] != '.'):
        for j in range(0,i,1):
            if (Dp1[j] == '.'):
                Dp1[i],Dp1[j] = Dp1[j],Dp1[i]
                
count = 0
for i in range(n):
    if (Dp1[i] != '.'):
        count += i*int(Dp1[i])
print(f"Part 1: {count}")

# Part 2

Dp2 = D2.copy()
n = len(D)
for i in range(n-1,-1,-2):
    bl = int(i/2)
    bn = D[i]
    for j in range(0,n_pos[bl]):
        if all(x == '.' for x in Dp2[j:j+bn]):
            Dp2[j:j+bn] = [str(bl)] * bn
            Dp2[n_pos[bl]:n_pos[bl]+bn] = '.' * bn
            break

count = 0
for i in range(len(Dp2)):
    if (Dp2[i] != '.'):
        count += i*int(Dp2[i])
print(f"Part 2: {count}")
