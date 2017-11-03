"""
Module Docstring
"""
import unittest
from heap_lab import MaxHeap


class TestHeap(unittest.TestCase):
    """
    Docstring
    """
    def test_insert(self):
        """
        Docstring
        """
        heap = MaxHeap(10)
        self.assertTrue(heap.is_empty())
        self.assertFalse(heap.is_full())
        for i in range(10):
            heap.insert(i)
        self.assertTrue(heap.is_full())
        self.assertFalse(heap.is_empty())

    def test_insert2(self):
        """
        Docstring
        """
        heap = MaxHeap()
        heap.insert(15)
        heap.insert(10)
        heap.insert(12)
        heap.insert(5)
        heap.insert(6)
        heap.insert(7)
        heap.insert(9)
        self.assertEqual(heap.heap_contents(), [15, 10, 12, 5, 6, 7, 9])

    def test_findmax(self):
        """
        Docstring
        """
        heap = MaxHeap(10)
        for i in range(10):
            heap.insert(i)
        self.assertEqual(heap.find_max(), 9)

    def test_get(self):
        """
        Docstring
        """
        heap = MaxHeap(10)
        for i in range(9):
            heap.insert(i)
        self.assertEqual(heap.get_heap_cap(), 10)
        self.assertEqual(heap.get_heap_size(), 9)
        self.assertFalse(heap.is_empty())
        self.assertFalse(heap.is_full())
        self.assertEqual(heap.heap_contents(), [8, 7, 5, 6, 2, 1, 4, 0, 3])

    def test_delete(self):
        """
        Docstring
        """
        heap = MaxHeap(10)
        for i in range(9):
            heap.insert(i)
        self.assertEqual(heap.del_max(), 8)
        self.assertEqual(heap.heap_contents(), [7, 6, 5, 3, 2, 1, 4, 0])

    def test_delete2(self):
        """
        Docstring
        """
        heap = MaxHeap()
        heap.insert(103)
        heap.insert(98)
        heap.insert(77)
        heap.insert(28)
        heap.insert(34)
        heap.insert(7)
        heap.insert(50)
        heap.insert(2)
        self.assertEqual(heap.heap_contents(), [103, 98, 77, 28, 34, 7, 50, 2])
        self.assertEqual(heap.del_max(), 103)
        self.assertEqual(heap.heap_contents(), [98, 34, 77, 28, 2, 7, 50])
    
    def test_dupli(self):
        """
        Docstring
        """

if __name__ == "__main__":
    unittest.main()
