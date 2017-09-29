class QueueArray:
	def __init__(self, capacity):
		self.capacity = capacity # the maximum number of items that can be stored in queue
		self.size = 0
		self.front = 0
		self.rear = 0
		self.items_arr=[None]*self.capacity
	def is_empty(self):
		return self.size == 0
	def is_full(self):
		return self.size == self.capacity
	def enqueue(self,item):
		if self.size == self.capacity:
			raise IndexError('Queue is full')
		self.items_arr[self.rear]=item
		self.rear+=1
		self.rear%=self.capacity
		self.size+=1
	def dequeue(self):
		if self.size == 0:
			raise IndexError('Queue is empty')
		temp = self.items_arr[self.front]
		self.front+=1
		self.front%=self.capacity
		self.size-=1
		return temp
	def num_in_queue(self):
		return self.size
		
class QueueLinked:
	def __init__(self,capacity):
		self.capacity = capacity
		self.front = None
		self.rear = None
		self.size = 0
	def is_empty(self):
		return self.size == 0
	def is_full(self):
		return self.size == self.capacity
	def enqueue(self,item):
		newNode = Node(item)
		if self.size == self.capacity:
			raise IndexError('Queue is full')
		if self.size == 0:
			self.front= newNode
		if self.rear is not None:
			self.rear=(self.rear).setNext(newNode)		
		self.rear= newNode
		self.size+=1
	

	def dequeue(self):
		temp = self.front
		if self.size == 0:
			raise IndexError('Queue is empty')
		if self.size == 1:
			self.front = None
			self.size-=1
			return temp.getData()
		self.front = (self.front).getNext()
		self.size-=1
		return temp.getData()
	def num_in_queue(self):
		return self.size
class Node:
	def __init__(self,initdata):
		self.data= initdata
		self.next=None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newdata):
		self.data = newdata
	def setNext(self,newdata):
		self.next = newdata