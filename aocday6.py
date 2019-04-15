cycles = 0

realloc = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
pastStates = []

def checkLists(L1,L2):
	for k in range(len(L1)):
		if(L1[k] != L2[k]):
			return False
	return True

def hasRepeat(pS):
	if(len(pS) >= 2):
		for i in range(0,len(pS) - 1):
				if(checkLists(pS[i],pS[len(pS) - 1]) is True):
					print ((len(pS) - 1) - i)
					return True
	return False

while(True):
	max_val = 0
	max_index = 0
	for i in range(0,len(realloc)):
		if(realloc[i] > max_val):
			max_val = realloc[i]
			max_index = i
	realloc[max_index] = 0
	list_pos = max_index + 1
	while(max_val > 0):
		if(list_pos > (len(realloc) - 1)): list_pos = 0
		realloc[list_pos] += 1
		max_val -= 1
		list_pos += 1
	pastStates.append(list(realloc))
	cycles += 1
	if(hasRepeat(pastStates) is True): break

#for i in range(len(pastStates)):
#	print pastStates[i]
print cycles