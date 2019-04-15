fname = "input_pass.txt"

numvalid = 0
phrase_dict = dict()

def _noRepeats_(line):
	phrase_dict.clear()
	for splits in (line.rstrip()).split(" "):
		sortW = ''.join(sorted(splits))
		if(phrase_dict.get(sortW) != None):
			return False
		phrase_dict[sortW] = 1
	return True

with open(fname) as f:
	for line in f:
		if(_noRepeats_(line)):
			numvalid += 1

print numvalid
