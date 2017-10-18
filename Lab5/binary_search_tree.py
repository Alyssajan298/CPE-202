class TreeNode:
	def __init__(self,key,data=None,left=None,right=None, parent=None):

		self.key = key
		self.data = None
		self.left = None
		self.right = None
		self.parent = None
	def insert(self,key):
		"""  Insert new node with key, assumes data not present """
		if self.key != None:
			if key < self.key:
				if self.left is None:
					self.left = TreeNode(key)
					self.left.parent = self
				else:
				   self.left.insert(key)
			elif key > self.key:
				if self.right is None:
					self.right = TreeNode(key)
					self.right.parent = self
				else:
					self.right.insert(key)
		else:
			self.key = key
	def find_successor(self):
		""" Finds the next successor of a TreeNode """
		if self.right == None:
			return self
		current = self.right
		while current.left != None:
			current = current.left
		return current
	def find_min(self):
		current = self
		while current.left != None:
			current = current.left
		return current.key
	def find_max(self):
		current = self
		while current.right != None:
			current = current.right
		return current.key
	def inorder_print_tree(self):
		"""   Print tree content inorder        """

		if (self.left != None):
			self.left.inorder_print_tree()

		print(self.key)

		if (self.right != None):
			self.right.inorder_print_tree()
	def print_levels(self):
		if (self.left != None):
			self.left.print_levels()

		count = 0
		start = self
		while start.parent != None:
			start = start.parent
		while self.key is not start.key:
			if self.key < start.key:
				count+=1
				start = start.left
			else:
				count+=1
				start = start.right

		# print "Value:",self.key,"Level:",count
		print [self.key,count]
		if (self.right != None):
			self.right.print_levels()
class BinarySearchTree:
	def __init__(self):
		self.root = None
	def find(self, key):
		p = self.root      # current node
		while p is not None and p.key != key :
			if key < p.key:
				p = p.left
			else:
				p = p.right

		if p is None :
			return False
		else:
			return True     # might want to return the node or ???

	def insert(self,newKey):
		if self.root is None:			 # if tree is empty
			self.root = TreeNode(newKey)
			return
		else:
			p = self.root
			if p.key > newKey:
				if p.left is None:
					p.left = TreeNode(newKey)
					p.left.parent = p
				else:
					p.left.insert(newKey)
			else:
				if p.right is None:
					p.right = TreeNode(newKey)
					p.right.parent = p
				else:
					p.right.insert(newKey)


	def delete(self,key):
		None
	def print_tree(self):
		None
	def is_empty(self):
		None
