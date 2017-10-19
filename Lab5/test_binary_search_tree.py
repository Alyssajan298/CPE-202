import unittest
from binary_search_tree import *

class testing_queues(unittest.TestCase):

	def test_given(self):
		'''Is the test that came with the template file'''
		self.printTestStart("given1")

		t = BinarySearchTree()
		t.insert(3)
		t.insert(10)
		t.insert(1)
		print ("Tree after inserting 8, 3, 10, 1")
		t.root.inorder_print_tree()
		t.insert(6)
		t.insert(4)
		t.insert(7)
		t.insert(14)
		t.insert(13)
		print ("Tree after inserting 6, 4, 7, 14, 13")
		t.root.inorder_print_tree()

		print("Testing find 14")
		print(t.find(14))
		print("Testing find 15")
		print(t.find(15))

	def test_given_printlevels(self):
		'''Modifies the given test to test print_levels() and is_empty'''
		self.printTestStart("given printlevels")

		t = BinarySearchTree()
		self.assertTrue(t.is_empty())
		t.insert(3)
		t.insert(10)
		t.insert(1)
		print ("Tree after inserting 8, 3, 10, 1")
		t.root.inorder_print_tree()
		t.insert(6)
		t.insert(4)
		t.insert(7)
		t.insert(14)
		t.insert(13)
		print ("Tree after inserting 6, 4, 7, 14, 13")
		t.root.inorder_print_tree()


		self.assertTrue(t.root.parent is None)

		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		print ("~~ LEVELS: ~~")
		t.root.right.print_levels()
		print ("~~ ~~")


		print("Testing find 14")
		print(t.find(14))
		print("Testing find 15")
		print(t.find(15))

	def test_find_successor(self):
		'''Tests find successor function in the node class'''
		self.printTestStart ("findsucc")

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
		'''Test the min/max finstions in the node class'''
		self.printTestStart ("minmax")

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


	def test_delete(self):
		'''Test the trees delete func when the removal is never the root'''
		self.printTestStart ("remove easy")

		t = BinarySearchTree()
		t.insert(20)
		t.insert(6)
		t.insert(29)
		t.insert(4)
		t.insert(3)
		t.insert(5)
		t.insert(8)
		t.insert(7)
		t.insert(9)
		t.insert(100)

		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")
		self.assertTrue(t.find(7))
		t.delete(7)
		self.assertFalse(t.find(7))


		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		self.assertTrue(t.find(8))
		t.delete(8)
		self.assertFalse(t.find(8))


		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		self.assertTrue(t.find(6))
		t.delete(6)
		self.assertFalse(t.find(6))

		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

	def test_remove_root(self):
		'''Test the trees delete func when the removal is the root'''

		self.printTestStart ("remove root")

		t = BinarySearchTree()
		t.insert(20)
		t.insert(6)
		t.insert(29)
		t.insert(4)
		t.insert(3)
		t.insert(5)
		t.insert(8)
		t.insert(7)
		t.insert(9)
		t.insert(100)

		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")
		self.assertTrue(t.find(20))
		t.delete(20)
		self.assertFalse(t.find(20))


		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		self.assertTrue(t.find(29))
		t.delete(29)
		self.assertFalse(t.find(29))


		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		self.assertTrue(t.find(100))
		t.delete(100)
		

		print ("~~ LEVELS: ~~")
		t.root.print_levels()
		print ("~~ ~~")

		self.assertFalse(t.find(100))

	def printTestStart(self,msg):
		'''Is called by each of the tests to make test output more readable'''
		print()
		print()
		print()
		print("!! TEST " + msg.upper() + " START:")
		print()



if __name__ == "__main__":
	unittest.main()

	
