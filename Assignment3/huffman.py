

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
		meme.left = node

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
	f = open(filename)
	countlist=[]
	for x in range(256):
		countlist.append(0)
	while True:
		c = f.read(1)
		if not c:
			break
		if ord(c) < 256:

			countlist[ord(c)] += 1
	f.close()
	return countlist
def create_huff_tree(char_freq):
	new_List= create_freq_list(char_freq)
	if len(new_List) is 0:
		return HuffmanNode(0,0)
	hufftree = None
	while len(new_List) != 1:
		i = find_min(new_List)
		node1 = new_List[i]
		del new_List[i]
		i = find_min(new_List)
		node2 = new_List[i]
		del new_List[i]
		hufftree = combine(node1,node2)
		new_List.append(hufftree)
	root = new_List[0]
	return root



def create_code (root_node):
	codelist=[]
	for x in range(256):
		codelist.append(None)
	recurse_code(root_node,"", codelist)
	return codelist
def recurse_code(node,current_code,codelist):
	if node.is_leaf() == False:
		recurse_code(node.left,current_code+"0",codelist)
		recurse_code(node.right,current_code+"1",codelist)
	else:
		node.set_code = current_code
		codelist[(node.char)]= current_code



createstr = ''
def tree_preord(node):
	global createstr
	createstr= ""
	recurse_tree(node)
	return createstr
def recurse_tree(node):
	global createstr
	if node != None:
		if node.is_leaf() == False:
			createstr = createstr + "0"
		elif node.is_leaf() == True:
			createstr = createstr +"1"
			createstr = createstr + chr(node.char)
		if node.left != None or node.right != None:
			recurse_tree(node.left)
			recurse_tree(node.right)




def huffman_encode(in_file, out_file):

	tree = create_huff_tree(cnt_freq(in_file))

	try:
		outf = open(out_file,'w')
	except:
		raise FileNotFoundError("input file not found")



	if tree.is_leaf() and tree.freq > 0:
		outf.write(chr(tree.char))
		outf.write(' ')
		outf.write(str(tree.freq))

	code = create_code(tree)

	try:
		inf = open(in_file,'r')
	except:
		raise FileNotFoundError("input file not found")

	while True:
		c = inf.read(1)
		if not c:
			break
		outf.write(str(code[ord(c)]))
	inf.close()
	outf.close()

def huffman_decode(freqs, encoded_file, decode_file):
	tree = create_huff_tree(freqs)
	codelist = create_code(tree)

	try:
		inf = open(encoded_file,'r')
		outf = open(decode_file,'w')
	except:
		raise FileNotFoundError("input file not found")

	codepart = ''
	while True:
		c = inf.read(1)
		if not c:
			break
		codepart += c
		if codepart in codelist:
			outf.write(chr(codelist.index(codepart)))
			codepart = ''
	inf.close()

	if tree.is_leaf() and tree.freq > 0:
		l = codepart.split()
		times = int(l[1])
		for i in range(times):
			outf.write(l[0])

	outf.close()
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
