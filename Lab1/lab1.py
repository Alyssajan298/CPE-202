def max_list_iter(n):
	if len(n)==0 :
		raise ValueError('This is an empty list')
	currentMax = n[0]
	for x in n:
		if currentMax < x:
			currentMax = x
	return(currentMax)
def reverse_rec(word):
	if len(word)==0 :
		return word
	x = len(word)-1
	if len(word) == 1 :
		return word
	return word[x] + reverse_rec(word[0:x])
def bin_search(target,low,high,list_val):
	
	if len(list_val)==0:
		return None
	if high<low :
		raise ValueError('Check your bounds')
	mid = (low+high)//2 
	if  high<= low and list_val[high]!=target:
			return None
	if list_val[mid] == target:
		return mid
	elif target > list_val[mid]:
		return bin_search(target,mid+1,high,list_val)
	elif target < list_val[mid]:
		return bin_search(target,low,mid-1,list_val)




