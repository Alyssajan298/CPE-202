import perm_lex
import unittest
class TestString(unittest.TestCase):
	#Tests when String is length 1
	def test_perm_lex(self):
			self.assertEqual(perm_lex.perm_gen_lex('c'),['c'])
	#Tests when String is length 2
	def test_perm_lex1(self):		
			self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
	#Tests when String is 'abc'
	def test_perm_lex2(self):		
			self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
	#Tests when String is empty
	def test_perm_lex3(self):
			with self.assertRaises(ValueError):
				perm_lex.perm_gen_lex('')
if __name__ == "__main__":
        unittest.main()	