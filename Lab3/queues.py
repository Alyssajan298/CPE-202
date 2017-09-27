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
		"""returns the number of items in the queue"""
# class QueueArray:
# 	None
# class QueueLinked:
# 	None