import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   print("testing testfile1.txt")

   def test_cnt_freq(self):
      freqlist	= cnt_freq("testfile1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104], "test_cnt_freq")

   def test_create_huff_tree(self):
      freqlist = cnt_freq("testfile1.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 32, "root freq check")
      self.assertEqual(hufftree.char, 97, "root char check")
      left = hufftree.left
      self.assertEqual(left.freq, 16, "root left child freq")
      self.assertEqual(left.char, 97, "root left child char")
      right = hufftree.right
      self.assertEqual(right.freq, 16, "root right child freq")
      self.assertEqual(right.char, 100, "root right child char")

   def test_create_code(self):
      freqlist = cnt_freq("testfile1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1', "file1 code for d check")
      self.assertEqual(codes[ord('a')], '0000', "file1 code for a check")
      self.assertEqual(codes[ord('f')], '0001', "file1 code for f check")

   def test_01_encodefile(self):
      huffman_encode("testfile1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"), "check file encodes correctly")

   def test_01_decodefile(self):
      freqlist = cnt_freq("testfile1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "decodefile1_soln.txt"), "check file decodes correctly")

class TestList2(unittest.TestCase):
   print("testing testfileChain.txt")

   def test_cnt_freq(self):
      freqlist = cnt_freq("testfileChain.txt")
      anslist = [0]*256
      anslist[97:107] = [1, 2, 4, 8, 0, 16, 32, 64, 0, 128] 
      self.assertListEqual(freqlist[97:104], anslist[97:104], "test_cnt_freq")

   def test_create_huff_tree(self):
      freqlist = cnt_freq("testfileChain.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 255, "root freq check")
      self.assertEqual(hufftree.char, 97, "root char check")
      left = hufftree.left
      self.assertEqual(left.freq, 127, "root left child freq")
      self.assertEqual(left.char, 97, "root left child char")
      right = hufftree.right
      self.assertEqual(right.freq, 128, "root right child freq")
      self.assertEqual(right.char, 106, "root right child char")

   def test_create_code(self):
      freqlist = cnt_freq("testfileChain.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '00001', "Chain code for d check")
      self.assertEqual(codes[ord('a')], '0000000', "Chain code for a check")
      self.assertEqual(codes[ord('j')], '1', "Chain code for j check")

   def test_01_encodefile(self):
      huffman_encode("testfileChain.txt", "outfileChain.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("outfileChain.txt", "outfileChain_soln.txt"), "check Chainfile encodes correctly")

   def test_01_decodefile(self):
      freqlist = cnt_freq("testfileChain.txt")
      huffman_decode(freqlist,"outfileChain.txt", "decodeChain.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodeChain.txt", "decodeChain_soln.txt"), "check Chainfile decodes correctly")

class TestList3(unittest.TestCase):
   print("testing testfileSameFreq.txt")

   def test_cnt_freq(self):
      freqlist = cnt_freq("testfileSameFreq.txt")
      anslist = [0]*256
      anslist[65:69] = [3, 3, 3, 3]
      anslist[97:114] = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
      self.assertEqual(freqlist[65:69], anslist[65:69], "test_cnt_freq part 1")
      self.assertEqual(freqlist[97:114], anslist[97:114], "test_cnt_freq part 2")

   def test_create_huff_tree(self):
      freqlist = cnt_freq("testfileSameFreq.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 63, "root freq check")
      self.assertEqual(hufftree.char, 65, "root char check")
      left = hufftree.left
      self.assertEqual(left.freq, 24, "root left child freq")
      self.assertEqual(left.char, 103, "root left child char")
      right = hufftree.right
      self.assertEqual(right.freq, 39, "root left child freq")
      self.assertEqual(right.char, 65, "root left child char")

   def test_create_code(self):
      freqlist = cnt_freq("testfileSameFreq.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('A')], '10110', "SameFreq code for A check")
      self.assertEqual(codes[ord('B')], '10111', "SameFreq code for B check")
      self.assertEqual(codes[ord('D')], '11001', "SameFreq code for D check")
      self.assertEqual(codes[ord('b')], '11011', "SameFreq code for b check")
      self.assertEqual(codes[ord('e')], '11110', "SameFreq code for e check")
      self.assertEqual(codes[ord('g')], '0000', "SameFreq code for g check")
      self.assertEqual(codes[ord('j')], '0011', "SameFreq code for j check")
      self.assertEqual(codes[ord('l')], '0101', "SameFreq code for l check")
      self.assertEqual(codes[ord('o')], '1000', "SameFreq code for o check")
      self.assertEqual(codes[ord('q')], '1010', "SameFreq code for q check")


   def test_01_encodefile(self):
      huffman_encode("testfileSameFreq.txt", "outfileSameFreq.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("outfileSameFreq.txt", "outfileSameFreq_soln.txt"), "check SameFreq encodes correctly")

   def test_01_decodefile(self):
      freqlist = cnt_freq("testfileSameFreq.txt")
      huffman_decode(freqlist,"outfileSameFreq.txt", "decodeSameFreq.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodeSameFreq.txt", "decodeSameFreq_soln.txt"), "check SameFreq decodes correctly")

class TestList4(unittest.TestCase):
   print("testing testfileWhiteSpace.txt")

   def test_cnt_freq(self):
      freqlist = cnt_freq("testfileWhiteSpace.txt")
      anslist = [0]*256
      anslist[10] = 3
      anslist[32:35] = [32, 1, 0, 4]
      anslist[49:54] = [1, 2, 4, 8, 16, 32]
      anslist[63:64] = [16, 2]
      anslist[94:103] = [8, 0, 0, 1, 2, 4, 8, 0, 16, 32]
      anslist[108:116] = [1, 2, 4, 0, 8, 0, 0, 16, 32]
      anslist[125] = 32
      self.assertEqual(freqlist[10], anslist[10], "test_cnt_freq part 1")
      self.assertEqual(freqlist[32:35], anslist[32:35], "test_cnt_freq part 2")
      self.assertEqual(freqlist[49:54], anslist[49:54], "test_cnt_freq part 3")
      self.assertEqual(freqlist[63:64], anslist[63:64], "test_cnt_freq part 4")
      self.assertEqual(freqlist[94:103], anslist[94:103], "test_cnt_freq part 5")
      self.assertEqual(freqlist[108:116], anslist[108:116], "test_cnt_freq part 6")
      self.assertEqual(freqlist[125], anslist[125], "test_cnt_freq part 7")

   def test_create_huff_tree(self):
      freqlist = cnt_freq("testfileWhiteSpace.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 287, "root freq check")
      self.assertEqual(hufftree.char, 10, "root char check")
      left = hufftree.left
      self.assertEqual(left.freq, 128, "root left child freq")
      self.assertEqual(left.char, 53, "root left child char")
      right = hufftree.right
      self.assertEqual(right.freq, 159, "root left child freq")
      self.assertEqual(right.char, 10, "root left child char")

   def test_create_code(self):
      freqlist = cnt_freq("testfileWhiteSpace.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('\n')], '1110000', "WhiteSpace code for '\\n' check")
      self.assertEqual(codes[ord(' ')], '1111', "WhiteSpace code for ' ' check")
      self.assertEqual(codes[ord('!')], '111000100', "WhiteSpace code for ! check")
      self.assertEqual(codes[ord('1')], '111000101', "WhiteSpace code for 1 check")
      self.assertEqual(codes[ord('4')], '111010', "WhiteSpace code for 4 check")
      self.assertEqual(codes[ord('6')], '001', "WhiteSpace code for 6 check")
      self.assertEqual(codes[ord('?')], '0001', "WhiteSpace code for ? check")
      self.assertEqual(codes[ord('^')], '01000', "WhiteSpace code for ^ check")
      self.assertEqual(codes[ord('d')], '01010', "WhiteSpace code for d check")
      self.assertEqual(codes[ord('g')], '100', "WhiteSpace code for g check")
      self.assertEqual(codes[ord('m')], '11101111', "WhiteSpace code for m check")
      self.assertEqual(codes[ord('n')], '010011', "WhiteSpace code for n check")
      self.assertEqual(codes[ord('s')], '0111', "WhiteSpace code for s check")
      self.assertEqual(codes[ord('}')], '110', "WhiteSpace code for } check")


   def test_01_encodefile(self):
      huffman_encode("testfileWhiteSpace.txt", "outfileWhiteSpace.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("outfileWhiteSpace.txt", "outfileWhiteSpace_soln.txt"), "check SameFreq encodes correctly")

   def test_01_decodefile(self):
      freqlist = cnt_freq("testfileWhiteSpace.txt")
      huffman_decode(freqlist,"outfileWhiteSpace.txt", "decodeWhiteSpace.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodeWhiteSpace.txt", "decodeWhiteSpace_soln.txt"), "check SameFreq decodes correctly")


if __name__ == '__main__': 
   unittest.main()


