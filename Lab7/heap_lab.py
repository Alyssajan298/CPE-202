"""
Implementation of a MaxHeap
"""


class MaxHeap(object):
    """
    MaxHeap Class Bottom-Up
    """
    def __init__(self, capacity=50):
        """
        Initialize class MaxHeap
        """
        self.scapacity = capacity
        self.size = 0
        self.heaplist = [None] * (capacity + 1)

    def insert(self, item):
        """
        Insert an element. Returns True/False
        if the insert is successful.
        """
        if self.size == len(self.heaplist):
            return False
        self.size += 1
        self.heaplist[self.size] = item
        self.perc_up(self.size)
        return True

    def find_max(self):
        """
        Returns the Maximum Value of the Heap
        """
        return self.heaplist[1]

    def del_max(self):
        """
        Returns the Maximum Value and deletes it
        """
        if self.size == 0:
            return
        maxim = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist[self.size] = maxim
        self.size -= 1
        self.perc_down(1)
        return maxim

    def heap_contents(self):
        """
        Returns the Heap List
        """
        arr = self.heaplist
        arr = arr[1:self.size+1]
        return arr

    def build_heap(self, alist):
        """
        Return True/False if build was successful. I.E. Returns
        False if list exceeds capacity of heap.
        """
        if self.get_heap_cap() < len(alist):
            return False
        index = 1
        for i in alist:
            self.heaplist[index] = alist[index-1]
            index += 1
            self.size += 1
        for i in range(self.get_heap_size()//2, 0, -1):
            self.perc_down(i)
        return True

    def is_empty(self):
        """
        Returns True/False if
        Heap is empty.
        """
        return self.size == 0

    def is_full(self):
        """
        Returns True/False if
        Heap is full.
        """
        return self.size == self.scapacity

    def get_heap_cap(self):
        """
        Returns the capacity of
        the Heap
        """
        return self.scapacity

    def get_heap_size(self):
        """
        Returns the current Size of
        the Heap
        """
        return self.size

    def perc_down(self, i):
        """
        Function that moves
        elements in Heap down.
        """
        current = self.heaplist[i]
        firstchild = self.heaplist[i * 2]
        secondchild = self.heaplist[i * 2 + 1]
       # if current <= firstchild or current <= secondchild:
        while self.qualify(i * 2, i * 2 + 1):
            if current <= firstchild or current <= secondchild:
                if secondchild == None:
                    temp = self.heaplist[i * 2]
                    self.heaplist[i * 2] = self.heaplist[i]
                    self.heaplist[i] = temp
                    break
                if firstchild > secondchild:
                    temp = self.heaplist[i * 2]
                    self.heaplist[i * 2] = self.heaplist[i]
                    self.heaplist[i] = temp
                    i = i * 2
                    current = self.heaplist[i]
                    firstchild = self.heaplist[i * 2]
                    secondchild = self.heaplist[i * 2 + 1]
                else:
                    temp = self.heaplist[i * 2 + 1]
                    self.heaplist[i * 2 + 1] = self.heaplist[i]
                    self.heaplist[i] = temp
                    i = i * 2 + 1
                    current = self.heaplist[i]
                    firstchild = self.heaplist[i * 2]
                    secondchild = self.heaplist[i * 2 + 1]
            else:
                break

    def qualify(self, child1, child2):
        """
        Helper Function for perc_down
        """
        if self.heaplist[child1] is not None and self.heaplist[child2] is None:
            if child1 <= self.size:
                return True
        elif self.heaplist[child1] is not None and self.heaplist[child2] is not None:
            if child1 <= self.size and child2 <= self.size:
                return True
        else:
            return False

    def perc_up(self, i):
        """
        Function that move
        elements in Heap up.
        """
        if i >= len(self.heaplist):
            raise IndexError
        compare = i // 2
        child = i
        while compare > 0 and self.heaplist[compare] <= self.heaplist[child]:
            temp = self.heaplist[compare]
            self.heaplist[compare] = self.heaplist[child]
            self.heaplist[child] = temp
            child = compare
            compare = compare // 2

    def heap_sort_increase(self, alist):
        """
        Sorts Given List Through the Use of Heaps
        """
        self.build_heap(alist)
        bigsize = self.get_heap_size()
        for i in range(bigsize):
            if self.size == 1:
                break
            self.del_max()
            print(self.heaplist)
        return self.heaplist[1:len(alist)+1]
alist = [1, 3, 2, 7, 4, 0, 5, 6]
heap = MaxHeap()
heap.heap_sort_increase(alist)
