from collections import defaultdict

with open("day17_input.txt") as f:
	inp = [r.strip('\n') for r in f]

nr,nc = len(inp), len(inp[0])

G = defaultdict(bool) # defaultfict returns False if key doesn't exist
for ix in range(0,nr):
	for iy in range(0,nc):
		G[(ix,iy,0)] = True if inp[ix][iy]=='#' else False

def numnear(x,y,z):
	n = 0
	for ix in range(x-1,x+2):
		for iy in range(y-1,y+2):
			for iz in range(z-1,z+2):
				if G[(ix,iy,iz)] and (ix,iy,iz)!=(x,y,z):
					n += 1
	return n

def Grange(G):
	tmp = list(G.keys())
	x1,x2,y1,y2,z1,z2 = 0,0,0,0,0,0
	for g in tmp:
		x1,x2 = min(x1,g[0]), max(x2,g[0])
		y1,y2 = min(y1,g[1]), max(y2,g[1])
		z1,z2 = min(z1,g[2]), max(z2,g[2])
	return ((x1,x2),(y1,y2),(z1,z2))

nc = 6
for i in range(nc):
	G2 = G.copy() # shallow copy is ok since values are scalars
	xx,yy,zz = Grange(G)
	for ix in range(xx[0]-1,xx[1]+2):
		for iy in range(yy[0]-1,yy[1]+2):
			for iz in range(zz[0]-1,zz[1]+2):
				if not (G[(ix,iy,iz)]==True and numnear(ix,iy,iz) in (2,3)):
					G2[(ix,iy,iz)] = False
				if (G[(ix,iy,iz)]==False) and (numnear(ix,iy,iz)==3):
					G2[(ix,iy,iz)] = True
				else:
					pass
	G = G2.copy()

print("Part 1: {}".format(sum(G.values())))



