inp = ['.#.', '..#', '###']

nr,nc = len(inp), len(inp[0])
xmin,xmax = 0,nc-1
ymin,ymax = 0,nr-1
zmin,zmax = 0,0

G = {}
for ix in range(xmin,xmax+1):
	for iy in range(ymin,ymax+1):
		G[(ix,iy)] = inp[ix][iy]

G2 = G.copy() # shallow copy is ok here since values are just character strings

def nearactive(G,x,y):
	n = 0
	#
	return n





