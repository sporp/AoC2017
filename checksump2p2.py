fname = "input_p2.txt"

checksum = 0

with open(fname) as f:
    for line in f:
	    smallest = 10000
	    largest = 0
	    arrlist = []
	    for splits in line.split("\t"):
	    	arrlist.append(int(splits))
	    arrlist.sort()
	    i = 0
	    while i < len(arrlist) - 1:
	    	j = i + 1
	    	while j < len(arrlist):
	    		if(arrlist[j]%arrlist[i] == 0):
	    			checksum += arrlist[j]/arrlist[i]
	    		j+=1
	    	i+=1

print checksum