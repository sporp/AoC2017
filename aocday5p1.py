fname = "jumplist.txt"

jumparray = []
currpos = 0
nextpos = 0
numjumps = 0

with open(fname) as f:
	for line in f:
		jumparray.append(int(line.rstrip('\n')))

listend = len(jumparray) - 1
while(currpos <= listend and currpos >= 0):
	nextpos = jumparray[currpos]
	if(jumparray[currpos] >= 3): jumparray[currpos] -= 1
	else: jumparray[currpos] += 1
	currpos += nextpos
	numjumps += 1

print numjumps