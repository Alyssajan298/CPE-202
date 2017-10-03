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
    # def remove(item):
    
    # def search_forward(item):
    
    # def search_backward(item):
    
    # def is_empty():
    
    def size(self):
        return self.capacity
    
    # def index(item):
    
    # def pop():
    
    # def pop(pos):

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