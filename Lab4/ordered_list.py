class OrderedList():

    def __init__(self):
        self.head = None
        self.capacity = 0
        self.tail = None


    def add(self,item):
        current= self.head
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

    
    # def search_forward(item):
    
    # def search_backward(item):
    
    def is_empty(self):
    	return self.capacity == 0
    
    def size(self):
        return self.capacity
    
    def index(self,item):
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
class Node:
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