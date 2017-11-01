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
        docstring
        """
        pass

    def del_max(self):
        """
        docstring
        """
        pass

    def heap_contents(self):
        """
        Returns the Heap List
        """
        return self.heaplist

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
        docstring
        """
        pass

    def get_heap_size(self):
        """
        docstring
        """
        pass

    def perc_down(self, i):
        """
        Function that moves
        elements in Heap down.
        """
        pass

    def perc_up(self, i):
        """
        Function that moves
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
