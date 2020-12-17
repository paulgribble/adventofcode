with open("day17_input_test.txt") as f:
	inp = [r.strip('\n') for r in f]

nr,nc = len(inp), len(inp[0])
x1,x2 = 0,nr-1
y1,y2 = 0,nc-1
z1,z2 = 0,0


o = (10,10,10)
import numpy as np
G = np.zeros((20,20,20))

for ix in range(x1,x2+1):
	for iy in range(y1,y2+1):
		for iz in range(z1,z2+1):
			G[ix+o[0],iy+o[1],iz+o[2]] = 0 if inp[ix][iy]=='.' else 1

def nearactive(G,o,p):
	x,y,z = p
	ix,iy,iz = o[0]+x, o[1]+y, o[2]+z
	n = sum(sum(sum(G[ix-1:ix+2,iy-1:iy+2,iz-1:iz+2] == 1)))
	if G[ix,iy,iz]==1:
		n = n - 1
	return n




mm = (x1,x2,y1,y2,z1,z2)

G = {}
for ix in range(x1,x2+1):
	for iy in range(y1,y2+1):
		G[(ix,iy,0)] = inp[ix][iy]

G2 = G.copy() # shallow copy is ok here since values are just character strings


def nearactive(G,x,y,z):
	n = 0
	
	return n




