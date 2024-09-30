# abbreviation.py

def abbreviation(word):
	x = len(word)
	y = x - 2
	letters = word.lower()
	if(x > 1):
		return '%s%s%s'%(letters[0], y, letters[x - 1])
	return letters
