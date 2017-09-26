import stacks
import unittest
class TestStacks(unittest.TestCase):
	
	def test_StackArray(self):
		
		arrStack = stacks.StackArray(5)
		self.assertEqual(arrStack.is_empty(), True) #Test empty stack
		arrStack.push(1) 
		self.assertEqual(arrStack.is_empty(), False) #Test empty stack with element inside stack
		self.assertEqual(arrStack.is_full(), False) #Test if stack is full
		arrStack.push(2)
		self.assertEqual(arrStack.size(),2) #Test the number of items
		arrStack.push(3)
		arrStack.push(4)
		arrStack.push(5)
		with self.assertRaises(IndexError): #Test if error is raised when going passed capacity
			arrStack.push(6) 
		self.assertEqual(arrStack.size(),5) 
		self.assertEqual(arrStack.is_full(), True) #Test when stack is full will confirm
		self.assertEqual(arrStack.pop(), 5) #Test return of top of stack and redirects top
		self.assertEqual(arrStack.size(),4) #Test to check the new size of stack
		self.assertEqual(arrStack.peek(),4) #Test new top of stack
		
		arrStack2 = stacks.StackArray(3)
		with self.assertRaises(IndexError):
			arrStack2.pop() #Test to pop an empty stack
		self.assertEqual(arrStack2.size(),0)#Test to return size of empty stack

	def test_StackLinked(self):
		nodestack = stacks.StackLinked(3) #Create Stacked Linked List
		with self.assertRaises(IndexError): #Tests Error, cannot pop an empty stack
			nodestack.pop()
		self.assertEqual(nodestack.is_empty(), True) #Tests if the stack is empty
		self.assertEqual(nodestack.size(), 0) #Tests if the size of the stack is 0
		nodestack.push(12) #Push first value to the stack
		self.assertEqual(nodestack.is_empty(), False) #Tests when something is pushed if the stack is empty
		self.assertEqual(nodestack.size(), 1)#Tests size function
		self.assertEqual(nodestack.peek(), 12)#Tests peek function
		self.assertEqual(nodestack.pop(), 12) #Tests pop function
		self.assertEqual(nodestack.peek(),None)#Tests peek function and returns None when there is nothing to peek
		self.assertEqual(nodestack.is_full(), False) #Tests if the Stack is full
		nodestack.push(15)
		nodestack.push(17)
		self.assertEqual(nodestack.size(), 2) #Tests the size after pushing 2 items
		self.assertEqual(nodestack.peek(),17) #Tests peek function
		self.assertEqual(nodestack.pop(),17) #Tests pop function 
		self.assertEqual(nodestack.peek(),15)#Tests peek to see if once the top is redirected if it returns the new top
		nodestack.push(12)
		nodestack.push(21)
		self.assertEqual(nodestack.size(), 3)
		self.assertEqual(nodestack.is_full(), True)#Tests when the Stack is full 
		with self.assertRaises(IndexError): #Tests pushing additional item after it is full
			nodestack.push(12)
		
	
		


if __name__ == "__main__":
        unittest.main()	