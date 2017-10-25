

class HuffmanNode:
	def __init__(self, char, freq):
		self.char = char  # actually the character code
		self.freq = freq
		self.code = None
		self.left = Nonex
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

def cnt_freq(filename):
	f = open(filename,encoding='utf-8-sig')
	countlist=[]
	for x in range(256):
		countlist.append(0)
	while True:
		c = f.read(1)
		if not c:
			print ("End of file")
			break
		countlist[ord(c)] += 1
	f.close()
	return countlist
def create_huff_tree(char_freq):
	pass
def create_code (node):
	pass
def tree_preord (node):
	pass
def huffman_encode(in_file, out_file):
	pass
def huffman_decode(freqs, encoded_file, decode_file):
	pass

cnt_freq('file1.txt')
