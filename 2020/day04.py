# load the data into a list

p = {}
docs = []
with open("day04_input.txt") as f:
	for line in f:
		if line=='\n':
			docs.append(p)
			p = {}
		else:
			fields = line.strip('\n').split(' ')
			for j in range(len(fields)):
				key,val = fields[j].split(':')
				p[key] = val
docs.append(p) # last one in case no newlines at end of file

# Part 1:

keys_req = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
valid = 0
for i in range(len(docs)):
	keys = set(docs[i].keys())
	ok = keys_req.difference(keys)==set() or keys_req.difference(keys)=={'cid'}
	if ok:
		valid += 1

print("Part 1: {}".format(valid))


# Part 2:

keys_req = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
hcl_req = set(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
ecl_req = ['amb','blu','brn','gry','grn','hzl','oth']
digits = ['0','1','2','3','4','5','6','7','8','9']
valid = 0
for i in range(len(docs)):
	keys = set(docs[i].keys())
	present = keys_req.difference(keys)==set() or keys_req.difference(keys)=={'cid'}
	if present:
		byr_ok = len(docs[i]['byr'])==4 and all(x in digits for x in docs[i]['byr']) and int(docs[i]['byr'])>=1920 and int(docs[i]['byr'])<=2002
		iyr_ok = len(docs[i]['iyr'])==4 and all(x in digits for x in docs[i]['iyr']) and int(docs[i]['iyr'])>=2010 and int(docs[i]['iyr'])<=2020
		eyr_ok = len(docs[i]['eyr'])==4 and all(x in digits for x in docs[i]['eyr']) and int(docs[i]['eyr'])>=2020 and int(docs[i]['eyr'])<=2030
		icm, iin = docs[i]['hgt'].find('cm'), docs[i]['hgt'].find('in')
		if icm>=1:
			hgt_ok = int(docs[i]['hgt'][0:icm])>=150 and int(docs[i]['hgt'][0:icm])<=193
		elif iin>=1:
			hgt_ok = int(docs[i]['hgt'][0:iin])>=59  and int(docs[i]['hgt'][0:iin])<=76
		else:
			hgt_ok = False
		hcl_ok = docs[i]['hcl'][0]=='#' and len(docs[i]['hcl'])==7 and all(x in hcl_req for x in docs[i]['hcl'][1:])
		ecl_ok = docs[i]['ecl'] in ecl_req
		pid_ok = len(docs[i]['pid'])==9 and all(x in digits for x in docs[i]['pid'])
		if all(x for x in [byr_ok, iyr_ok, eyr_ok, hgt_ok, hcl_ok, ecl_ok, pid_ok]):
			valid += 1

print("Part 2: {}".format(valid))

