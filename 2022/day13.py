# PART 1
#

def readpacket(file):
    p1 = file.readline().strip("\n")
    p2 = file.readline().strip("\n")
    _ = file.readline()
    p1 = eval(p1)
    p2 = eval(p2)
    return p1,p2


def compare(pp1,pp2):
    print(f"compare {pp1} vs {pp2}")
    if (isinstance(pp1,int) and isinstance(pp2,int)):
        return (pp1 <= pp2)
    else:
        if (not isinstance(pp1,list)): pp1 = [pp1]
        if (not isinstance(pp2,list)): pp2 = [pp2]
        if ((len(pp1)==0) and (len(pp2)==0)):  return True
        elif ((len(pp1)==0) and (len(pp2)>0)): return True
        elif ((len(pp1)>0) and (len(pp2)==0)): return False
        else:
            if (len(pp1)>1):
                return (compare(pp1[0],pp2[0])) and compare(pp1[1:],pp2[1:])
            else:
                return (compare(pp1[0],pp2[0]))
    
file = open("day13_input_test.txt", 'r')
isum = 1
i = 1
p1,p2 = readpacket(file)
isum += (compare(p1,p2)==1) * i

while (p1):
    i += 1
    p1,p2 = readpacket(file)
    isum += (compare(p1,p2)==1) * i
file.close()

print(f"Part 1: the answer is {isum}")
