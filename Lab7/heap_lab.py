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
            raise IndexError
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
        docstring
        """
        pass

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
        while (i * 2) <= self.size and (i * 2 + 1) <= self.size:
            if self.heaplist[i * 2] >= self.heaplist[i * 2 + 1]:
                temp = self.heaplist[i * 2]
                self.heaplist[i * 2] = self.heaplist[i]
                self.heaplist[i] = temp
                i = i * 2
            else:
                temp = self.heaplist[i * 2 + 1]
                self.heaplist[i * 2 + 1] = self.heaplist[i]
                self.heaplist[i] = temp
                i = i * 2 + 1

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
        docstring
        """
        pass
