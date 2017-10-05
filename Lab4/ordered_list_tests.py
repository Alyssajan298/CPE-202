import unittest
from ordered_list import *
class Test_OrderedList(unittest.TestCase):
	''' Tests the add function '''
	def test_add0(self):
		g = OrderedList()
		self.assertTrue(g.is_empty(),True)
		g.add(1)
		self.assertFalse(g.is_empty(),False)
		self.assertEqual(g.head.getData(),1)
		self.assertEqual(g.tail.getData(),1)
		self.assertEqual(g.size(),1)
		g.add(0)
		self.assertEqual(g.head.getData(),0)
		self.assertEqual(g.tail.getData(),1)
		self.assertEqual(g.size(),2)
		g.add(2)
		self.assertEqual(g.head.getData(),0)
		self.assertEqual(g.tail.getData(),2)
		self.assertEqual(g.size(),3)
	''' Tests the add function with end cases (head and tail exceptions) '''
	def test_add1(self):
		h = OrderedList()
		self.assertTrue(h.is_empty(),True)
		h.add(1)
		h.add(2)
		self.assertFalse(h.is_empty(),False)
		self.assertEqual(h.head.getData(),1)
		self.assertEqual(h.tail.getData(),2)
		self.assertEqual(h.size(),2)
		h.add(0)
		self.assertEqual(h.head.getData(),0)
		self.assertEqual(h.size(),3)
		h.add(4)
		self.assertEqual(h.tail.getData(),4)
		self.assertEqual(h.size(),4)
		h.add(3)
		self.assertEqual(h.tail.getPrev().getData(),3)
		self.assertEqual(h.head.getNext().getData(),1)
		self.assertEqual(h.size(),5)
		h.add(0.5)
		self.assertEqual(h.head.getNext().getData(),0.5)
		self.assertEqual(h.head.getNext().getNext().getData(),1)
		self.assertEqual(h.head.getNext().getNext().getNext().getData(),2)
		self.assertEqual(h.head.getNext().getNext().getNext().getNext().getData(),3)
		self.assertEqual(h.head.getNext().getNext().getNext().getNext().getNext().getData(),4)
		self.assertEqual(h.size(),6)
if __name__ == "__main__":
	unittest.main()


