import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
	def test_cnt_freq(self):
		freqlist= cnt_freq("file1.txt")
		anslist = [0]*256
		anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
		self.assertListEqual(freqlist[97:104], anslist[97:104])
	def test_find_min(self):
		freqlist = cnt_freq("file1.txt")
		anslist = create_freq_list(freqlist)
		temp = find_min(anslist)
		self.assertEqual((anslist[temp]).char, ord('a'))
	def test_find_min1(self):
		nodelist = create_freq_list(cnt_freq("file1.txt"))
		self.assertTrue(len(nodelist) < 250)
		for node in nodelist:
			self.assertNotEqual(node.freq,0)

		freqchars = ['a','f','b','c','d']
		for f in freqchars:
			i = find_min(nodelist)
			self.assertEqual(nodelist[i].char,ord(f))
			del nodelist[i]
	def test_create_huff_tree(self):
		freqlist = cnt_freq("file1.txt")
		hufftree = create_huff_tree(freqlist)
		numchars = 32
		charforroot = "a"
		self.assertEqual(hufftree.freq, 32)
		self.assertEqual(hufftree.char, 97)
		left = hufftree.left
		self.assertEqual(left.freq, 16)
		self.assertEqual(left.char, 97)
		right = hufftree.right
		self.assertEqual(right.freq, 16)
		self.assertEqual(right.char, 100)
	def test_create_code(self):
	  freqlist = cnt_freq("file1.txt")
	  hufftree = create_huff_tree(freqlist)
	  codes = create_code(hufftree)
	  self.assertEqual(codes[ord('d')], '1')
	  self.assertEqual(codes[ord('a')], '0000')
	  self.assertEqual(codes[ord('f')], '0001')

	def test_01_encodefile(self):
	  huffman_encode("file1.txt", "output1.txt")
	  # capture errors by running 'filecmp' on your encoded file
	  # with a *known* solution file
	  self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))

	def test_01_decodefile(self):
	  freqlist = cnt_freq("file1.txt")
	  huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
	  # capture errors by running 'filecmp' on your encoded file
	  # with a *known* solution file
	  self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))
	def test_shrek(self):
		freqlist = cnt_freq("shrek.txt")
		huffman_encode("shrek.txt", "shrek.huf")
		huffman_decode(freqlist,"shrek.huf","shrekREWINDHUF.txt")
		self.assertTrue(filecmp.cmp("shrek.txt", "shrekREWINDHUF.txt"))
	def test_smash(self):
		freqlist = cnt_freq("smash.txt")
		huffman_encode("smash.txt", "smash.huf")
		huffman_decode(freqlist,"smash.huf","smashREWIND.txt")
		self.assertTrue(filecmp.cmp("smash.txt", "smashREWIND.txt"))
	def test_wonky(self):
		freqlist = cnt_freq("exclaim.txt")
		huffman_encode("exclaim.txt", "exclaim.huf")
		huffman_decode(freqlist,"exclaim.huf","exclaimREWIND.txt")
		self.assertTrue(filecmp.cmp("exclaim.txt", "exclaimREWIND.txt"))
	def test_ez_preord(self):
		build = tree_preord(create_huff_tree(cnt_freq("file1.txt")))
		expectstring = '00001a1f1b1c1d'
		self.assertEqual(len(expectstring),len(build))
		for i in range(len(build)):
			self.assertEqual(expectstring[i],build[i])
	def test_empty_testfile(self):
		open('empty_file.txt', 'a').close()
		freqlist = cnt_freq("empty_file.txt")
		huffman_encode("empty_file.txt", "empty.huf")
		huffman_decode(freqlist,"empty.huf","emptyREWIND.txt")
		self.assertTrue(filecmp.cmp("empty_file.txt", "emptyREWIND.txt"))

	def test_file_not_exist(self):
		with self.assertRaises(FileNotFoundError):
			freqlist = cnt_freq("DNE.txt")
		with self.assertRaises(FileNotFoundError):
			huffman_encode("DNE.txt","N/A")
		with self.assertRaises(FileNotFoundError):
			huffman_decode(cnt_freq("file1.txt"),"DNE.txt","N/A")


if __name__ == '__main__':
   unittest.main()
