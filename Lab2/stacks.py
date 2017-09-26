class StackArray:
	def __init__(self, capacity):
		
		self.capacity = capacity
		self.items= [None]*capacity
		self.num_items = 0
		
	def is_empty(self):
		if self.num_items==0:
			return True
		else:
			return False
	def is_full(self):
		if self.num_items==self.capacity:
			return True
		else:
			return False
	def push(self, item):
		if self.num_items==self.capacity:
			raise IndexError('The Stack is Full')
		self.items[self.num_items]=item
		self.num_items+=1		
	def pop(self):
		if self.num_items == 0:
			raise IndexError('The Stack is Empty')
		popped = self.items[self.num_items-1]
		self.num_items-=1
		return popped
	def peek(self): 
		return self.items[self.num_items-1]
	def size(self): 
		return self.num_items
class Node:
	def __init__(self,initdata):
		self.data=initdata
		self.next=None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newdata):
		self.data= newdata
	def setNext(self,newnext):
		self.next = newnext
class StackLinked:
	def __init__(self,capacity):
		self.capacity= capacity
		self.top= None
		self.count= 0
	def is_empty(self):
		return self.count == 0
	def is_full(self):
		return self.count == self.capacity
	def push(self,data):
		newNode = Node(data)
		if self.count == self.capacity:
			raise IndexError('The Stack is Full')
		if self.count== 0:
			newNode.setNext(None)
		newNode.setNext(self.top)
		self.top = newNode
		self.count+=1
	def pop(self):
		if self.count == 0:
			raise IndexError('The Stack is Empty')
		temp = self.top.getData()

		self.top = (self.top.getNext())
		self.count-=1
		return temp
	def peek(self):
		if self.count == 0:
			return None
		return self.top.getData()
	def size(self):
		return self.count



