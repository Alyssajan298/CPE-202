"""
Test Cases
"""
import unittest
from random import randint
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
        self.assertEqual(hashtbl.collisions(), 0)
        self.assertEqual(hashtbl.load_factor(), 0.2)
    
    def test_hash2(self):
        """
        Tests Hash Table #2
        """
        hashtbl = MyHashTable()
        hashtbl.insert(20, 15)
        self.assertEqual(hashtbl.get(20), (20, 15))
        hashtbl.insert(20, 45)
        self.assertEqual(hashtbl.get(20), (20, 45))
        self.assertEqual(hashtbl.size(), 1)
        self.assertEqual(hashtbl.remove(20), (20, 45))
        self.assertEqual(hashtbl.size(), 0)
        self.assertEqual(hashtbl.collisions(), 1)
        hashtbl.insert(20, 15)
        hashtbl.insert(9, 67)
        self.assertEqual(hashtbl.get(9), (9, 67))
        self.assertEqual(hashtbl.size(), 2)
        self.assertEqual(hashtbl.remove(9), (9, 67))
        self.assertEqual(hashtbl.collisions(), 2)

    def test_random(self):
        """
        Tests Random Hash
        """
        hashtbl = MyHashTable(5)
        for x in range(21):
            y = randint(0, 100)
            z = randint(0, 10)
            hashtbl.insert(y, z)

    def test_rehash(self):
        """
        Tests Rehash
        """
        hashtbl = MyHashTable(3)
        hashtbl.insert(3, 15)
        hashtbl.insert(4, 51)
        hashtbl.insert(5, 72)
        hashtbl.insert(9, 67)
        hashtbl.insert(10, 56)
        self.assertEqual(len(hashtbl.hashlist), 7)
        hashtbl.insert(21, 67)
        self.assertEqual(hashtbl.collisions(), 2)

    def test_collision(self):
        """
        Tests Collision Cases
        """
        hashtbl = MyHashTable(10)
        hashtbl.insert(10, 'apple')
        hashtbl.insert(20, 'banana')
        hashtbl.insert(30, 'pineapple')
        hashtbl.insert(40, 'tomato')
        hashtbl.insert(1, 'teeth')
        hashtbl.insert(11, 'eyes')
        self.assertEqual(hashtbl.collisions(), 7)


if __name__ == "__main__":
    unittest.main()
