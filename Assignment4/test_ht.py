import unittest
from hash_lin_table import *
from random import randint
import filecmp
import os

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

	def test_readstopwords(self):
		ht = HashTableLinPr()
		ht.read_stop('stop_words.txt')
		# print(ht.arr)
		self.assertTrue(ht.contains('the'))

	def test_insert_nostop_harder_withlast(self):
		ht = HashTableLinPr()
		ht.read_file('input2.txt',None)
		# for thing in ht.arr:
		# 	if thing is not None:
		# 		print(thing[0])
		self.assertTrue(ht.contains('some'))
		self.assertTrue(ht.contains('punctuation'))
		self.assertTrue(ht.contains('is'))
		self.assertTrue(ht.contains('on'))
		self.assertTrue(ht.contains('line'))
		self.assertFalse(ht.contains('2'))
		self.assertFalse(ht.contains('s'))
		self.assertTrue(ht.contains('quicksorts'))
		self.assertFalse(ht.contains('quicksort\'s'))
		self.assertFalse(ht.contains('African'))
		self.assertTrue(ht.contains('african'))
		self.assertTrue(ht.contains('consuming'))
		self.assertListEqual(ht.get_lines('earthquake'),[2])
		self.assertTrue(ht.contains('american'))
		self.assertFalse(ht.contains('American'))

	def test_insert_nostop_harder_nolast(self):
		ht = HashTableLinPr()
		ht.read_file('input2.txt',None)
		# for thing in ht.arr:
		# 	if thing is not None:
		# 		print(thing[0])
		self.assertTrue(ht.contains('some'))
		self.assertTrue(ht.contains('punctuation'))
		self.assertTrue(ht.contains('is'))
		self.assertTrue(ht.contains('on'))
		self.assertTrue(ht.contains('line'))
		self.assertFalse(ht.contains('2'))
		self.assertFalse(ht.contains('s'))
		self.assertTrue(ht.contains('quicksorts'))
		self.assertFalse(ht.contains('quicksort\'s'))
		self.assertFalse(ht.contains('African'))
		self.assertTrue(ht.contains('african'))
		self.assertTrue(ht.contains('consuming'))
		self.assertListEqual(ht.get_lines('earthquake'),[2])

	def test_insert_nostop_ez(self):
		ht = HashTableLinPr()
		ht.read_file('input2.txt',None)
		# for thing in ht.arr:
		# 	if thing is not None:
		# 		print(thing[0])
		self.assertTrue(ht.contains('some'))
		self.assertTrue(ht.contains('punctuation'))
		self.assertTrue(ht.contains('is'))
		self.assertTrue(ht.contains('on'))
		self.assertTrue(ht.contains('line'))
		self.assertFalse(ht.contains('2'))
		self.assertFalse(ht.contains('s'))
		self.assertTrue(ht.contains('quicksorts'))
		self.assertFalse(ht.contains('quicksort\'s'))
		self.assertFalse(ht.contains('African'))
		self.assertTrue(ht.contains('african'))
		self.assertTrue(ht.contains('consuming'))
		self.assertListEqual(ht.get_lines('earthquake'),[2])
		self.assertFalse(ht.contains(''))

	def test_insert_with_stoptable_withlast(self):
		stop = HashTableLinPr()
		stop.read_stop("stop_words.txt")
		ht = HashTableLinPr()
		ht.read_file("input2.txt", stop)
		self.assertFalse(ht.contains('some'))
		self.assertTrue(ht.contains('punctuation'))
		self.assertFalse(ht.contains('is'))
		self.assertFalse(ht.contains('on'))
		self.assertFalse(ht.contains('line'))
		self.assertFalse(ht.contains('2'))
		self.assertFalse(ht.contains('s'))
		self.assertTrue(ht.contains('quicksorts'))
		self.assertFalse(ht.contains('quicksort\'s'))
		self.assertFalse(ht.contains('African'))
		self.assertTrue(ht.contains('african'))
		self.assertTrue(ht.contains('consuming'))
		self.assertListEqual(ht.get_lines('earthquake'),[2])
		self.assertListEqual(ht.get_lines('punctuation'),[1])
		self.assertTrue(ht.contains('american'))
		self.assertFalse(ht.contains('American'))

	def test_insert_with_stoptable_nolast(self):
		stop = HashTableLinPr()
		stop.read_stop("stop_words.txt")
		ht = HashTableLinPr()
		ht.read_file("input2.txt", stop)
		self.assertFalse(ht.contains('some'))
		self.assertTrue(ht.contains('punctuation'))
		self.assertFalse(ht.contains('is'))
		self.assertFalse(ht.contains('on'))
		self.assertFalse(ht.contains('line'))
		self.assertFalse(ht.contains('2'))
		self.assertFalse(ht.contains('s'))
		self.assertTrue(ht.contains('quicksorts'))
		self.assertFalse(ht.contains('quicksort\'s'))
		self.assertFalse(ht.contains('African'))
		self.assertTrue(ht.contains('african'))
		self.assertTrue(ht.contains('consuming'))
		self.assertListEqual(ht.get_lines('earthquake'),[2])
		self.assertListEqual(ht.get_lines('punctuation'),[1])

	def test_correct_linnums_last_word_in_line(self):
		stop = HashTableLinPr()
		stop.read_stop("stop_words.txt")
		ht = HashTableLinPr()
		ht.read_file("input1.txt", stop)
		self.assertFalse(ht.contains('some'))
		self.assertTrue(ht.contains('correctly'))
		self.assertFalse(ht.contains('is'))
		self.assertFalse(ht.contains('on'))
		self.assertFalse(ht.contains('line'))
		self.assertFalse(ht.contains('2'))
		self.assertFalse(ht.contains('s'))
		self.assertTrue(ht.contains('earthquake'))
		self.assertFalse(ht.contains('quicksort\'s'))
		self.assertFalse(ht.contains('African'))
		self.assertTrue(ht.contains('handled'))
		self.assertTrue(ht.contains('fourscore'))
		self.assertListEqual(ht.get_lines('earthquake'),[1])
		self.assertListEqual(ht.get_lines('correctly'),[3])

	def test_sorted(self):
		stop = HashTableLinPr()
		stop.read_stop("stop_words.txt")
		ht = HashTableLinPr()
		ht.read_file("input2.txt", stop)

	def test_completetest_input1(self):
		stop = HashTableLinPr()
		stop.read_stop("stop_words.txt")
		ht = HashTableLinPr()
		ht.read_file("input1.txt", stop)
		ht.save_concordance("concord1-result.txt")
		self.files_differ("concord1-result.txt","concord1.txt")

	def test_completetest_input2(self):
		stop = HashTableLinPr()
		stop.read_stop("stop_words.txt")
		ht = HashTableLinPr()
		ht.read_file("input2.txt", stop)
		ht.save_concordance("concord2-result")
		self.files_differ("concord2-result","concord2.txt")

	def test_black(self):
		stop = HashTableLinPr()
		stop.read_stop("stop.txt")
		ht = HashTableLinPr()
		ht.read_file("black.txt", stop)
		ht.save_concordance("concord-black")

	def files_differ(self,first,second):
		f = open(first,"r")
		s = open(second,"r")
		while True:
			c = f.read(1)
			d = s.read(1)
			if c != d:
				self.assertEqual(c,d)
			if not c or not d:
				break
		f.close()
		s.close()

if __name__ == "__main__":
	unittest.main()

	
