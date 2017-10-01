def perm_gen_lex(word):
	
	lister=[]
	if len(word) == 0:
		raise ValueError('This is an empty string')
	if len(word) == 1:
		return [word]
	for x in word:
		rem_ele=""
		for y in word:
			if(y!=x):
				rem_ele+=y
		z= perm_gen_lex(rem_ele)
		for w in z:
			lister.append(x+w)
	return lister










