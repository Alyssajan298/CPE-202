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


if __name__ == "__main__":
    unittest.main()
