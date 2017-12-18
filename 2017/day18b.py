
# Part 2 - some parts of the implementation adapted from vash3r

def Rint(c):
	if ((ord(c[0])<=ord('z')) & (ord(c[0])>=ord('a'))):
		return r[c]
	else:
		return int(c)

lines = [l.strip('\n') for l in open('day18_input.txt')]
ll = len(lines)

R1 = {} # program 1 register
R2 = {} # program 2 register
for i in range(26):
    R1[chr(ord('a')+i)] = 0
    R2[chr(ord('a')+i)] = 0
R2['p'] = 1
Rs = [R1,R2] # collect the two registers together

tot = 0 # num times program 1 sent a value
ind = [0,0] # each program's instruction index
snd = [[],[]] # data queues
state = ['ok','ok'] # {ok,r,done} (r=receiving)
pr = 0 # current program
r = Rs[pr] # pointer to current registers
i = ind[0] # pointer to current instruction

stop = False
while (stop==False):
	if (pr==0): # define the index of the other program
		pr_o = 1
	else:
		pr_o = 0
	l = lines[i].split()
	if (l[0]=='set'):
		r[l[1]] = Rint(l[2])
	elif (l[0]=='add'):
		r[l[1]] += Rint(l[2])
	elif (l[0]=='mul'):
		r[l[1]] *= Rint(l[2])
	elif (l[0]=='snd'): # send
		if (pr==1): # count how many times program 1 sends
			tot += 1
		snd[pr].append(Rint(l[1]))
	elif (l[0]=='mod'):
		r[l[1]] = r[l[1]] % Rint(l[2])
	elif (l[0]=='rcv'):
		if (len(snd[pr_o]) > 0): # other program has sent some data
			state[pr] = 'ok'
			r[l[1]] = snd[pr_o].pop(0) # put the data into the register
		else: # wait: switch to other prog
			if (state[pr_o]=='done'):
				stop = True # we are waiting but other prog has terminated
			if ((len(snd[pr])==0) & (state[pr_o]=='r')):
				stop = True # we are not sending but other prog is waiting
			if (stop==True):
				break # might as well break out now if we're deadlocked
			ind[pr] = i # save index
			state[pr] = 'r' # save state
			if (pr==0): # toggle to other program
				pr = 1
			else:
				pr = 0
			i = ind[pr] - 1 # increment back
			r = Rs[pr]    # point to other program's registers
	elif (l[0]=='jgz'):
		if (Rint(l[1]) > 0):
			i += Rint(l[2]) - 1
	i += 1
	if ((i<0) | (i>=ll)): # we've jumped outside the instructions
		if (state[pr_o] == 'done'): # is the other program done too?
			stop = True # both programs are terminated
		else:
			state[pr] = 'done' # we are done
			ind[pr] = i  # swap back since other program's not done
			if (pr==0): # toggle to other program
				pr = 1
			else:
				pr = 0
			i = ind[pr]
			r = Rs[pr]

print('day 2: program 1 sent a value {} times'.format(tot))



