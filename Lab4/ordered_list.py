class OrderedList():

	def __init__(self):
		self.head = None
		self.capacity = 0
		self.tail = None


	def add(self,item):
		'''Adds item to the list at the proper place so it remains sorted'''
		'''Assume that the item is not already in the list'''
		'''Takes an item and returns nothing'''
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item: 
				stop = True
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if self.capacity == 0:
			temp.setNext(None)
			temp.setPrev(None)
			self.head = temp
			self.tail = temp
		elif previous == None:
			temp.setNext(self.head)
			if self.capacity == 1:
				self.tail = self.head
			self.head.setPrev(temp)
			self.head = temp
		elif current == None:
			temp.setPrev(self.tail)
			self.tail.setNext(temp)
			self.tail = temp
			self.tail.setNext(None)
		else:
			temp.setNext(current)
			temp.setPrev(previous)
			previous.setNext(temp)
			current.setPrev(temp)
		self.capacity+=1
	def remove(self,item):
		'''Removes item from the list'''
		'''Assumes that the item is in the list'''
		'''Doesn't return anything'''
		index = 0
		start = self.head
		while index < self.capacity:
			if start.getData() == item:
				if self.capacity == 1:
					self.head = None
					self.tail = None
				elif index == 0: 
					self.head = start.getNext()
				elif index == self.capacity-1:
					start.getPrev().setNext(None)
					self.tail = start.getPrev()
				else:
					start.getNext().setPrev(start.getPrev())
					start.getPrev().setNext(start.getNext())
				self.capacity-=1
				break
			else:
				start = start.getNext()
				index+=1    
	def search_forward(self,item):
		'''Searches for the item by starting at the head'''
		'''Returns True if the item is in the list'''
		index = 0
		start = self.head
		while index < self.capacity:
			if start.getData() == item:
				return True
			else:
				start = start.getNext()
				index+=1
		return False
	def search_backward(self,item):
		'''Searches for the item by starting at the tail'''
		'''Returns True if the item is in the list'''
		index = self.capacity -1 
		start = self.tail
		while index >= 0:
			if start.getData() == item:
				return True
			else:
				start = start.getPrev()
				index-=1 
		return False  
	def is_empty(self):
		'''Returns if the list is empty (size == 0)'''
		return self.capacity == 0
	
	def size(self):
		'''Returns the size of the list'''
		return self.capacity
	
	def index(self,item):
		'''Returns the index of the item'''
		'''Assumes that the item is in the list'''
		index = 0
		start = self.head
		while index < self.capacity:
			if start.getData() == item:
				return index
			else:
				start= start.getNext()
				index += 1
	def pop(self,pos=None):
		'''Removes and returns the item at the given position'''
		'''Position defaults to the last position is not given'''
		'''Removes and returns the item at the given position by searching from front if pos <= size//2'''
		'''And from rear if pos > size//2'''
		if pos is None:
			temp = self.tail.getData()
			self.tail = self.tail.getPrev()
			if self.capacity == 1:
				return temp
			self.tail.setNext(None)
			self.capacity-=1
			return temp
		index = 0
		start = self.head
		if pos <= self.capacity//2: 
			while index < self.capacity:
				if index == pos:
					temp = start.getData()
					if self.capacity == 1:
						self.head = None
						self.tail = None
					elif index == 0: 
						self.head = start.getNext()
					elif index == self.capacity-1:
						start.getPrev().setNext(None)
						self.tail = start.getPrev()
					else:
						start.getNext().setPrev(start.getPrev())
						start.getPrev().setNext(start.getNext())
					self.capacity-=1
					return temp
				
				else:
					start = start.getNext()
					index+=1
		elif pos > self.capacity//2:
			index = self.capacity -1 
			start = self.tail
			while index >= 0:
				if index == pos:
					temp = start.getData()
					if self.capacity == 1:
						self.head = None
						self.tail = None
					elif index == 0: 
						self.head = start.getNext()
					elif index == self.capacity-1:
						start.getPrev().setNext(None)
						self.tail = start.getPrev()
					else:
						start.getPrev().setNext(start.getNext())
						start.getNext().setPrev(start.getPrev())
						
					self.capacity-=1
					return temp
				else:
					start = start.getPrev()
					index-=1

class Node:
	'''Node that contains references to the next and previous node for use in a doubly-linked list'''
	def __init__(self,initdata):
		self.data=initdata
		self.next=None
		self.prev=None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def getPrev(self):
		return self.prev
	def setData(self,newdata):
		self.data= newdata
	def setNext(self,newnext):
		self.next = newnext
	def setPrev(self,newprev):
		self.prev = newprev