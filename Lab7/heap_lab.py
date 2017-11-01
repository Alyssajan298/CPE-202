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
        self.size = 0
        self.heaplist = [capacity]

    def insert(self, item):
        """
        Insert an element. Returns True/False
        if the insert is successful.
        """
        if self.size == len(self.heaplist):
            return False
        self.heaplist.append(item)
        self.size += 1
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
        docstring
        """
        pass

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
        return self.size == len(self.heaplist)

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
        pass

    def heap_sort_increase(self, alist):
        """
        docstring
        """
        pass
