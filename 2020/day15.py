def speak(N,n):
    pos = {}
    for i in range(len(N)-1):
pos[N[i]] = i # position
s = N[-1]
i = len(N)-1
for i in range(i,n-1):
    if s not in pos.keys():
        pos[s] = i
        s = 0
        N.append(s)
    else:
        snew = i-pos[s]
        N.append(snew)
        pos[s] = i
        s = snew
        if int(i/n*100)%5==0:
            print("{:3}%".format(int(i/n*100)), end='\r')
            return s

            print("Part 1: {}".format(speak([15,5,1,4,7,0],2020)))

            print("Part 2: {}".format(speak([15,5,1,4,7,0],30000000)))
