import queues 
import unittest

class TestLab3(unittest.TestCase):
	def test_QueueArray(self):
		q1 = queues.QueueArray(4)
		self.assertEqual(q1.is_empty(),True) #Checks is_empty method on an empty Queue
		with self.assertRaises(IndexError): #Checks if raises IndexError when dequeuing a Queue
			q1.dequeue()
		q1.enqueue(1)
		self.assertEqual(q1.num_in_queue(),1) #Checks the number of items in Queue
		self.assertEqual(q1.items_arr,[1,None,None,None]) #Checks if enqueue worked 
		self.assertEqual(q1.is_empty(),False) #Checks is_empty method on a Queue that has called enqueue once
		self.assertEqual(q1.is_full(),False) #Checks is_full method on a Queue that has called enqueue once
		q1.enqueue(2)
		self.assertEqual(q1.num_in_queue(),2) #Checks the number of items in Queue
		q1.enqueue(3)
		q1.enqueue(4)
		with self.assertRaises(IndexError): #Checks if raises IndexError when enqueuing a full Queue
			q1.enqueue(5)
		self.assertEqual(q1.is_full(),True) #Checks is_full method on a Queue when all slots are occupied by elements
		self.assertEqual(q1.num_in_queue(),4) #Checks the number of items in Queue

	def test_QueueLinked(self):
		None

if __name__=="__main__":
	unittest.main()
