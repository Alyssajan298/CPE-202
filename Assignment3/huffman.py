

class HuffmanNode:
	def __init__(self, char, freq):
		self.char = char  # actually the character code
		self.freq = freq
		self.code = None
		self.left = None
		self.right = None

	def set_code (self, code):
		self.code = code

	def set_left (self, node):
		self.left = node

	def set_right (self, node):
		self.right = node
	def is_leaf(self):
		return self.left is None and self.right is None





def comes_before (a, b) :
	"""returns true if tree rooted at node a comes before tree rooted at node b """
	if a.freq == b.freq:
		return a.char < b.char
	else:
		return a.freq < b.freq
def combine (a, b) :
	""" creates a new huffman node with children a and b with combined freq with name of the left child """
	if not comes_before(a,b):
		raise AssertionError("A must come before b when calling combine")
	c = None
	if a.char <  b.char:
		c = a.char
	else:
		c= b.char
	f = a.freq + b.freq
	par = HuffmanNode(c,f)
	par.left = a
	par.right = b
	return par
def cnt_freq(filename):
	f = open(filename,encoding='utf-8-sig')
	countlist=[]
	for x in range(256):
		countlist.append(0)
	while True:
		c = f.read(1)
		if not c:
			break
		countlist[ord(c)] += 1
	f.close()
	return countlist
def create_huff_tree(char_freq):
	new_List= create_freq_list(char_freq)
	hufftree = None
	while len(new_List) != 1:
		i = find_min(new_List)
		node1 = new_List[i]
		del new_List[i]
		i = find_min(new_List)
		node2 = new_List[i]
		del new_List[i]
		hufftree = combine(node1,node2)
		node1.code = 0
		node2.code = 1
		new_List.append(hufftree)
	root = new_List[0]
	root.set_left(node1)
	root.set_right(node2)
	return root



def create_code (root_node):
	pass
def tree_preord (node):
	pass
def huffman_encode(in_file, out_file):
	pass
def huffman_decode(freqs, encoded_file, decode_file):
	pass
def find_min(nodelist):
	current_min= nodelist[0]
	index = 1
	saveindex= 0
	while index < len(nodelist):
		if comes_before(nodelist[index],current_min):
			current_min = nodelist[index]
			saveindex= index
		index+=1
	# return current_min
	return saveindex
def create_freq_list(countlist):
	nodelist = []
	for i in range(len(countlist)):
			if countlist[i] > 0:
				nodelist.append(HuffmanNode(i,countlist[i]))
	return nodelist


cnt_freq('file1.txt')
