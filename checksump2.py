fname = "input_p2.txt"

checksum = 0

with open(fname) as f:
    for line in f:
	    smallest = 10000
	    largest = 0
	    for splits in line.split("\t"):
	    	curr = int(splits)
	    	if(curr < smallest):
	    		smallest = curr
	    	if(curr > largest):
	    		largest = curr
	    checksum += largest - smallest

print checksum