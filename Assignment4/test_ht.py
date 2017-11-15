import unittest
from hash_lin_table import *
from random import randint

class testing_heaps(unittest.TestCase):

	def test_myhash(self):
		ht = HashTableLinPr()
		self.assertEqual(ord('c'),ht.myhash('c',251))
		self.assertNotEqual(ord('z'),ht.myhash('c',251))
		self.assertNotEqual(ord('C'),ht.myhash('c',251))

		ords = []
		string = 'papa'
		for c in string:
			ords.append(ord(c))

		prop = ords[0] * (31**3) + ords[1] * (31**2) + ords[2] * (31) + ords[3]
		prop %= 251
		self.assertEqual(prop,ht.myhash(string,251))

		strlist = ['papa', "lmao", 'zzzzzzzzzzzzzzz', 'l33t', '&ds234**wdfa::']
		for string in strlist:
			prop = 0
			big = min(len(string),8)
			for i in range(big):
				prop += (31 ** (big-(1+i))) * ord(string[i])
			prop %= 251
			self.assertEqual(prop,ht.myhash(string,251))
			if big < 8:
				self.assertNotEqual(prop,ht.myhash(string+'z',251))
			else:
				self.assertEqual(prop,ht.myhash(string+'z',251))

	def test_stops(self):
		ht = HashTableLinPr()
		ht.read_stop('stop_words.txt')




	# def test_init(self):
	# 	ht = MyHashTable()
	# 	for i in range(len(ht.arr)):
	# 		self.assertEqual(ht.arr[i], [])

	# def test_insert_and_rehash(self):
	# 	ht = MyHashTable()
	# 	print(ht.arr)
	# 	for i in range(len(ht.arr) * 2):
	# 		ht.insert(i,i*2)
	# 	print(ht.arr)
	# 	ht.insert(3,9999999)
	# 	print(ht.arr)
		
	# def test_hash(self):
	# 	"""
	# 	Tests Hash Table #1
	# 	"""
	# 	hashtbl = MyHashTable(5)
	# 	hashtbl.insert(2, 3)
	# 	self.assertEqual(hashtbl.arr[2], [(2, 3)])
	# 	self.assertEqual(hashtbl.get(2), (2, 3))
	# 	with self.assertRaises(LookupError):
	# 		hashtbl.get(1)
	# 	self.assertEqual(hashtbl.size(), 1)
	# 	self.assertEqual(hashtbl.collisions(), 0)
	# 	self.assertEqual(hashtbl.load_factor(), 0.2)
	   
	# def test_hash2(self):
	# 	"""
	# 	Tests Hash Table #2
	# 	"""
	# 	hashtbl = MyHashTable()
	# 	hashtbl.insert(1, 11)
	# 	self.assertEqual(hashtbl.get(1), (1, 11))
	# 	hashtbl.insert(1, 11)
	# 	self.assertEqual(hashtbl.get(1), (1, 11))
	# 	self.assertEqual(hashtbl.size(), 1)
	# 	self.assertEqual(hashtbl.remove(1), (1, 11))
	# 	self.assertEqual(hashtbl.size(), 0)
	# 	self.assertEqual(hashtbl.collisions(), 1)
	# 	hashtbl.insert(3, 33)
	# 	hashtbl.insert(9, 99)
	# 	self.assertEqual(hashtbl.get(9), (9, 99))
	# 	self.assertEqual(hashtbl.size(), 2)
	# 	self.assertEqual(hashtbl.remove(9), (9, 99))
	# 	self.assertEqual(hashtbl.collisions(), 1)

	# def test_random(self):
	# 	"""
	# 	Tests Random Hash
	# 	"""
	# 	l = []
	# 	hashtbl = MyHashTable(5)
	# 	count = 0
	# 	for x in range(21):
	# 		y = randint(0, 100)
	# 		z = randint(0, 10)
	# 		if y in l:
	# 			count -= 1
	# 		count += 1
	# 		l.append(y)
	# 		hashtbl.insert(y, z)
	# 	self.assertEqual(hashtbl.size(),count)

	# def test_collision(self):
	# 	"""
	# 	Tests Collision Cases
	# 	"""
	# 	hashtbl = MyHashTable(10)
	# 	hashtbl.insert(30, 2)
	# 	hashtbl.insert(40, 3)
	# 	hashtbl.insert(60, 4)
	# 	hashtbl.insert(80, 5)
	# 	hashtbl.insert(33, 11)
	# 	hashtbl.insert(333, 111)
	# 	self.assertEqual(hashtbl.collisions(), 7)



if __name__ == "__main__":
	unittest.main()

	
