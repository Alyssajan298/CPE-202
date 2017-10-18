import unittest
from binary_search_tree import *

class testing_queues(unittest.TestCase):
	def test_given(self):
		t = BinarySearchTree()
		t.insert(3)
		t.insert(10)
		t.insert(1)
		t.insert(2)
		t.insert(0.5)
		t.insert(2.5)
		# print ("Tree after inserting 8, 3, 10, 1")
		# t.root.inorder_print_tree()
		t.insert(6)
		t.insert(4)
		t.insert(7)
		t.insert(14)
		t.insert(13)
		# print ("Tree after inserting 6, 4, 7, 14, 13")
		# t.root.inorder_print_tree()
		# t.root.right.inorder_print_tree()


		self.assertTrue(t.root.parent is None)

		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		# print ("~~ LEVELS: ~~")
		# t.root.right.print_levels()
		# print ("~~ ~~")


		"""Testing find 14"""
		self.assertTrue(t.find(14))
		"""Testing find 15"""
		self.assertFalse(t.find(15))
		"""Testing finding root"""
		self.assertTrue(t.find(t.root.key))

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
