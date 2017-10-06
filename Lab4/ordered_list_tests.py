import unittest
from ordered_list import *
class Test_OrderedList(unittest.TestCase):
	''' Tests the add function '''
	def test_add0(self):
		g = OrderedList()
		self.assertTrue(g.is_empty())
		g.add(1)
		self.assertEqual(g.index(1),0)
		g.remove(1)
		self.assertEqual(g.head, None)
		self.assertEqual(g.tail, None)
		self.assertTrue(g.is_empty())
		g.add(1)
		self.assertEqual(g.index(1),0)
		self.assertFalse(g.is_empty(),False)
		self.assertEqual(g.head.getData(),1)
		self.assertEqual(g.tail.getData(),1)
		self.assertEqual(g.size(),1)
		g.add(0)
		self.assertEqual(g.index(1),1)
		self.assertEqual(g.index(0),0)
		self.assertEqual(g.head.getData(),0)
		self.assertEqual(g.tail.getData(),1)
		self.assertEqual(g.size(),2)
		g.add(2)
		self.assertEqual(g.index(2),2)
		self.assertEqual(g.head.getData(),0)
		self.assertEqual(g.tail.getData(),2)
		self.assertEqual(g.size(),3)
		g.remove(0)
		self.assertEqual(g.head.getData(),1)
		g.add(0)
		g.remove(2)
		self.assertEqual(g.tail.getData(),1)
		g.add(2)
		self.assertFalse(g.is_empty())
		g.remove(1)
		self.assertEqual(g.index(2),1)
		g.remove(0)
		g.remove(2)
		self.assertTrue(g.is_empty())
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
		self.assertEqual(h.index(4),3)
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
	def test_array_endpop(self):
		"""Tests the add and pops without an argument"""
		l = OrderedList()
		self.assertTrue(l.is_empty())
		l.add(1)
		l.add(2)
		self.assertFalse(l.is_empty())
		l.add(3)
		l.add(4)
		self.assertFalse(l.is_empty())
		self.assertEqual(l.index(3),2)
		
		self.assertEqual(l.pop(),4)
		self.assertEqual(l.pop(),3)

		self.assertEqual(l.pop(),2)
		self.assertEqual(l.pop(),1)
	def test_array_harder_pop(self):
		"""Tests add and pops from front and end of the list"""
		l = OrderedList()
		self.assertTrue(l.is_empty())
		l.add(1)
		l.add(2)
		self.assertFalse(l.is_empty())
		l.add(3)
		l.add(4)
		
		self.assertEqual(l.pop(0),1)
		self.assertEqual(l.pop(2),4)
		self.assertEqual(l.pop(1),3)
		self.assertEqual(l.pop(),2)
	def test_array_hardest_pop(self):
		"""Tests adding out of order and popping from front and end of the lsit"""
		l = OrderedList()
		self.assertTrue(l.is_empty())
		l.add(1)
		l.add(5)
		self.assertFalse(l.is_empty())
		l.add(4)
		l.add(3)
		l.add(2)
		
		self.assertEqual(l.pop(),5)
		self.assertEqual(l.pop(1),2)
		self.assertEqual(l.pop(),4)
		self.assertEqual(l.pop(0),1)
		self.assertEqual(l.pop(),3)





if __name__ == "__main__":
	unittest.main()


