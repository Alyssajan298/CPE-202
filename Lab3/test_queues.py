import queues 
import unittest

class TestLab3(unittest.TestCase):
	def test_QueueArray(self):
		
		"""Tests normal execution on an array-based implementation"""
		# q = queues.QueueArray(5)
		# self.assertTrue(q.is_empty())
		# with self.assertRaises(IndexError):
		# 	q.dequeue()
		# q.enqueue(1)
		# self.assertEqual(q.dequeue(),1)
		# self.assertTrue(q.is_empty())
		# q.enqueue('a')
		# q.enqueue('b')
		# self.assertEqual(q.num_in_queue(),2)
		# self.assertFalse(q.is_empty())
		# self.assertFalse(q.is_full())
		# q.enqueue('c')
		# q.enqueue('d')
		# q.enqueue('e')
		# with self.assertRaises(IndexError):
		# 	q.enqueue('f')
		# self.assertTrue(q.is_full())
		# self.assertFalse(q.is_empty())
		# self.assertEqual(5,q.num_in_queue())
		# self.assertEqual(q.dequeue(),'a')
		# self.assertEqual(q.dequeue(),'b')
		# self.assertEqual(q.dequeue(),'c')
		# self.assertEqual(q.dequeue(),'d')
		# self.assertEqual(q.dequeue(),'e')
		# self.assertTrue(q.is_empty())
		# self.assertFalse(q.is_full())
		# q.enqueue('a')
		# q.enqueue('b')
		# q.enqueue('c')
		# q.enqueue('d')
		# q.enqueue('e')
		# self.assertEqual(q.dequeue(),'a')
		# q.enqueue('f')
		# self.assertEqual(q.dequeue(),'b')
		# self.assertEqual(q.dequeue(),'c')
		# q.enqueue('g')
		# self.assertEqual(q.dequeue(),'d')
		# self.assertEqual(q.dequeue(),'e')
		# self.assertEqual(q.dequeue(),'f')

		q1 = queues.QueueArray(4)
		self.assertEqual(q1.is_empty(),True) #Checks is_empty method on an empty Queue
		q1.enqueue(1)
		self.assertEqual(q1.num_in_queue(),1) #Checks the number of items in Queue
		self.assertEqual(q1.items_arr,[1,None,None,None]) #Checks if enqueue worked 
		self.assertEqual(q1.is_empty(),False) #Checks is_empty method on a Queue that has called enqueue once
		self.assertEqual(q1.is_full(),False)
		q1.enqueue(2)
		self.assertEqual(q1.num_in_queue(),2) #Checks the number of items in Queue
		q1.enqueue(3)
		q1.enqueue(4)
		self.assertEqual(q1.is_full(),True)
		self.assertEqual(q1.num_in_queue(),4) #Checks the number of items in Queue
		print q1.items_arr
		
	def test_QueueLinked(self):
		None

if __name__=="__main__":
	unittest.main()
