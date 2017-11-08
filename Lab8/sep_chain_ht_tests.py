"""
Test Cases
"""
import unittest
from sep_chain_ht import MyHashTable


class TestHash(unittest.TestCase):
    """
    Test Cases for Hash Table
    """
    def test_hash(self):
        """
        Tests Hash Table #1
        """
        hashtbl = MyHashTable(5)
        hashtbl.insert(5, 21)
        self.assertEqual(hashtbl.hashlist[0], [(5, 21)])
        self.assertEqual(hashtbl.get(5), (5, 21))
        with self.assertRaises(LookupError):
            hashtbl.get(6)
        self.assertEqual(hashtbl.size(), 1)

if __name__ == "__main__":
    unittest.main()
