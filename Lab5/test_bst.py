import unittest
from binary_search_tree import *

class testing_queues(unittest.TestCase):
	# def test_given(self):
	# 	t = BinarySearchTree()
	# 	t.insert(3)
	# 	t.insert(10)
	# 	t.insert(1)
	# 	t.insert(2)
	# 	t.insert(0.5)
	# 	t.insert(2.5)
	# 	print ("Tree after inserting 3,10,1,2,0.5,2.5")
	# 	t.root.inorder_print_tree()
	# 	t.insert(6)
	# 	t.insert(4)
	# 	t.insert(7)
	# 	t.insert(14)
	# 	t.insert(13)
	# 	print ("Tree after inserting 6, 4, 7, 14, 13")
	# 	t.root.inorder_print_tree()
	# 	t.root.right.inorder_print_tree()
	# 	self.assertTrue(t.root.parent is None)
	# 	print ("~~ LEVELS: ~~")
	# 	t.root.print_levels()
	# 	print ("~~ ~~")
	# 	print ("~~ LEVELS (Right): ~~")
	# 	t.root.right.print_levels()
	# 	print ("~~ ~~")
	# 	t.print_tree()
	# 	"""Testing find 14"""
	# 	self.assertTrue(t.find(14))
	# 	"""Testing find 15"""
	# 	self.assertFalse(t.find(15))
	# 	"""Testing finding root"""
	# 	self.assertTrue(t.find(t.root.key))
	# def test_delete_empty_noChild(self):
	# 	t = BinarySearchTree()
	# 	self.assertTrue(t.is_empty())
	# 	t.insert(10)
	# 	self.assertFalse(t.is_empty())
	# 	t.insert(3)
	# 	t.insert(21)
	# 	t.root.inorder_print_tree()
	# 	t.delete(21)
	# 	t.print_tree()
	# 	t.delete(3)
	# 	t.print_tree()
	# 	t.delete(10)
	# 	self.assertTrue(t.is_empty())
	# def test_delete_empty_oneChild(self):
		# t = BinarySearchTree()
		# t.insert(10)
		# t.insert(3)
		# t.insert(21)
		# t.insert(27)
		# print t.root.right.key
		# print t.root.right.right.key
		# print t.root.right.right.parent.key
		# t.delete(21)
		# print t.root.right.key
		# print t.root.right.parent.key
		# tr = BinarySearchTree()
		# tr.insert(10)
		# tr.insert(3)
		# tr.insert(21)
		# tr.insert(27)
		# tr.insert(1)
		# tr.print_tree()
		# tr.delete(3)
		# tr.print_tree()
		# print tr.root.left.key
		# print tr.root.left.parent.key
		# tre = BinarySearchTree()
		# tre.insert(10)
		# tre.insert(21)
		# tre.insert(27)
		# tre.print_tree()
		# tre.delete(10)
		# tre.print_tree()
		# print tre.root.key
		# tree = BinarySearchTree()
		# tree.insert(10)
		# tree.insert(3)
		# tree.insert(1)
		# tree.print_tree()
		# tree.delete(10)
		# tree.print_tree()
		# print tree.root.key
	def test_delete_empty_twoChild(self):
		# t = BinarySearchTree()
		# t.insert(10)
		# t.insert(21)
		# t.insert(27)
		# t.insert(3)
		# t.insert(1)
		# t.insert(16)
		# t.insert(4)
		# print '                     ', t.root.key
		# print '                    ',t.root.left.key,t.root.right.key
		# print '                  ',t.root.left.left.key,t.root.left.right.key,t.root.right.left.key,t.root.right.right.key
		# t.delete(10)
		#
		# print '                     ', t.root.key
		# print '                    ',t.root.left.key,t.root.right.key
		# print '                  ',t.root.left.left.key,t.root.left.right.key,' ' ,t.root.right.right.key
		t = BinarySearchTree()
		t.insert(10)
		t.insert(21)
		t.insert(27)
		t.insert(3)
		t.insert(1)
		t.insert(16)
		t.insert(5)
		t.insert(0)
		t.insert(2)
		t.insert(4)
		t.insert(6)
		t.insert(14)
		t.insert(20)
		t.insert(23)
		t.insert(30)
		print ('                     ', t.root.key)
		print ('                    ',t.root.left.key,t.root.right.key)
		print ('                  ',t.root.left.left.key,t.root.left.right.key,t.root.right.left.key,t.root.right.right.key)
		print ('             ', t.root.left.left.left.key, t.root.left.left.right.key, t.root.left.right.left.key, t.root.left.right.right.key, t.root.right.left.left.key, t.root.right.left.right.key, t.root.right.right.left.key, t.root.right.right.right.key)


		t.delete(16)
		print ('                     ', t.root.key)
		print ('                    ',t.root.left.key,t.root.right.key)
		print ('                  ',t.root.left.left.key,t.root.left.right.key,t.root.right.left.key,t.root.right.right.key)
		print ('             ', t.root.left.left.left.key, t.root.left.left.right.key, t.root.left.right.left.key, t.root.left.right.right.key, t.root.right.left.left.key,t.root.right.right.left.key, t.root.right.right.right.key)

	def test_find_successor(self):
		t = BinarySearchTree()
		t.insert(3)
		t.insert(10)
		t.insert(1)
		t.insert(6)
		self.assertEqual(t.root.find_successor().key,6)
		t.insert(4)
		self.assertEqual(t.root.find_successor().key,4)
		t.insert(5)
		self.assertEqual(t.root.find_successor().key,4)
		self.assertEqual(t.root.key,3)

	def test_minmax(self):
		t = BinarySearchTree()
		t.insert(3)
		self.assertEqual(t.root.find_min(),3)
		self.assertEqual(t.root.find_max(),3)
		t.insert(10)
		self.assertEqual(t.root.find_min(),3)
		self.assertEqual(t.root.find_max(),10)
		t.insert(1)
		self.assertEqual(t.root.find_min(),1)
		self.assertEqual(t.root.find_max(),10)
		t.insert(6)
		self.assertEqual(t.root.find_min(),1)
		self.assertEqual(t.root.find_max(),10)
		self.assertEqual(t.root.right.find_min(),6)
		self.assertEqual(t.root.find_max(),10)
		self.assertEqual(t.root.find_successor().key,6)
		t.insert(4)
		self.assertEqual(t.root.find_successor().key,4)
		t.insert(5)
		self.assertEqual(t.root.find_successor().key,4)
		self.assertEqual(t.root.key,3)



if __name__ == "__main__":
	unittest.main()
