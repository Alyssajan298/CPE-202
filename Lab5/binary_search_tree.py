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
		""" Finds the smallest key value of the Tree """
		current = self
		while current.left != None:
			current = current.left
		return current.key
	def find_max(self):
		""" Finds the largest key value of the Tree """
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
		""" Print [key, level of node] inorder """
		start = self
		while start.parent != None:
			start = start.parent

		if (self.left != None) and self.left.key is not start.key:
			self.left.print_levels()
		count = 0
		
		while self.key is not start.key:
			if self.key < start.key:
				count+=1
				start = start.left
			else:
				count+=1
				start = start.right
		print ([self.key,count])
		if (self.right != None)  and self.right.key is not start.key:
			self.right.print_levels()
class BinarySearchTree:
	def __init__(self):
		self.root = None
	def find(self, key):
		""" Finds given key value and returns True/False whether if in Tree """
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
		""" Beginning of insert function to input nodes onto Tree """
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
		p = self.root
		while p.key != key :
			if key < p.key:
				p = p.left
			else:
				p = p.right
		self.delete_node(p)

	def delete_node(self,p):
		print("^^^&#W*&")
		""" Deletes TreeNodes according to key value. """
		#NoChild Case
		if p.left == None and p.right == None:
			if p.key == self.root.key:
				self.root = None
			elif p.parent.left== p:
				p.parent.left = None
			else:
				p.parent.right = None
		#OneChild Case
		elif p.left == None or p.right == None:
			if p.key == self.root.key:
				print ("@@@")
				if self.root.left != None:
					self.root = self.root.left
					self.root.parent= None
				else:
					self.root = self.root.right
					self.root.parent= None
			elif p.left != None:
				p.left.parent = p.parent
				if p.key < p.parent.key:
					p.parent.left = p.left
				else:
					p.parent.right = p.left
			else:
				p.right.parent = p.parent
				if p.key > p.parent.key:
					p.parent.right = p.right
				else:
					p.parent.left = p.right
		#TwoChild Case
		else:
			if p.key == self.root.key:
				print("??")
				print(p.left.key)
				print(p.right.key)
				temp = self.root.find_successor()
				self.delete_node(temp)
				p.key = temp.key
				# saveleft= self.root.left
				# saveright= self.root.right
				# self.root = temp
				# self.root.left=saveleft
				# self.root.right=saveright
				# self.root.parent= None
			else:
				temp = p.find_successor()
				self.delete_node(p.find_successor())
				saveleft = p.left
				saveright = p.right
				temp.parent = p.parent
				if p.parent.right == p:
					p.parent.right = temp
				else:
					p.parent.left = temp
				p = temp
				p.left = saveleft
				p.right = saveright
	def print_tree(self):
		""" Prints the entire tree inorder """
		root = self.root
		if (root.left != None):
			root.left.inorder_print_tree()

		print(root.key)

		if (root.right != None):
			root.right.inorder_print_tree()
	def is_empty(self):
		""" Returns True/False if Tree is empty """
		return self.root == None
