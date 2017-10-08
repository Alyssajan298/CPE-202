import unittest
from exp_eval import * 

class test_expressions(unittest.TestCase):
	def test_invalid(self):
		'''Tests Invalid Postfix Expressions'''
		self.assertFalse(postfix_valid(""))
		self.assertFalse(postfix_valid("2 3"))
		self.assertFalse(postfix_valid("+ 2 3"))
		self.assertFalse(postfix_valid("2 - 3 +"))
 
	def test_valid(self):
		'''Tests Validity of Postfix Expressions'''
		self.assertTrue(postfix_valid("2 3 +"))
		self.assertTrue(postfix_valid("4 2 5 * +"))
		self.assertTrue(postfix_valid("2 3 -"))
		self.assertTrue(postfix_valid("2 3 *"))
		self.assertTrue(postfix_valid("2 3 /"))
		self.assertTrue(postfix_valid("2 3 ^"))
		self.assertTrue(postfix_valid("2 3 + 4 -"))
		self.assertTrue(postfix_valid("1.0 2.0 -"))
		self.assertTrue(postfix_valid("4 5 + 3 * 5 6 - 4 5 + * -"))

	def test_postfixeval1(self):
		'''Tests Postfix Evaluation'''
		self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
		self.assertAlmostEqual(postfix_eval("5 3 -"), 2.0)
		self.assertAlmostEqual(postfix_eval("5 3 /"), 1.6666666666666667)
		self.assertAlmostEqual(postfix_eval("4 5 + 3 * 5 6 - 4 5 + * -"), 36)
		self.assertAlmostEqual(postfix_eval("27 26 - 45 *"), 45) 
		self.assertAlmostEqual(postfix_eval("3 2 ^"), 9)
		self.assertFalse(postfix_valid("2 3 + + 4 6 +"))
		self.assertEqual(infix_to_postfix("6 / ( 3 / 2 * ( 5 + 7 ) )"), "6 3 2 / 5 7 + * /")
		self.assertEqual(infix_to_postfix("6 ^ ( 3 / ( 2 + 5 + 7 ) )"), "6 3 2 5 + 7 + / ^")
		with self.assertRaises(ValueError):
			postfix_eval("5 0 /")
		'''Tests Postfix Evaluation'''
	
	"""Tests Infix to Postfix"""
	def test_inToPostBasicAssoc(self):
		self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
	def test_inToPostBasicAssoc1(self):
		self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")
	def test_inToPostBasicAssoc2(self):
		self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")
	def test_inToPostBasicAssoc2_1(self):
		self.assertEqual(infix_to_postfix("4 + 2 * 5"), "4 2 5 * +")
	def test_inToPostBasicAssoc2_2(self):
		self.assertEqual(infix_to_postfix("4 * 2 + 5"), "4 2 * 5 +")
	def test_inToPostBasicAssoc2_3(self):
		self.assertEqual(infix_to_postfix("4 ^ 3 * 5 / 2"), "4 3 ^ 5 * 2 /")
	def test_inToPostBasicAssoc2_4(self):
		self.assertEqual(infix_to_postfix("4 ^ 3 * 5 / 2 + 6"), "4 3 ^ 5 * 2 / 6 +")
	def test_inToPostBasicAssoc2_5(self):
		self.assertEqual(infix_to_postfix("3 * 5 / 2 ^ 3"), "3 5 * 2 3 ^ /")
	def test_inToPostBasicAssoc2_6(self):
		self.assertEqual(infix_to_postfix("3 * 5 - 4 / 2 ^ 3 + 7"), "3 5 * 4 2 3 ^ / - 7 +")
	def test_inToPostBasicAssoc3(self):
		self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")
	
	"""Tests Infix to Postfix"""
	
	def test_inToPostBasicAssoc5(self):
		''' Tests division by zero '''
		self.assertEqual(infix_to_postfix("6"), "6")
		with self.assertRaises(ValueError): 
			postfix_eval("3 0 /")
	
	def test_simple_add1(self):
		'''Tests conversion and evaluation of simple addition'''
		self.assertEqual(infix_to_postfix("3 + 4"),"3 4 +")
		self.assertEqual(postfix_eval("3 4 +"),7)
		self.assertEqual(postfix_eval(infix_to_postfix("3 + 4")),7)
# 
	def test_simple_ooo4(self):
		'''Tests conversion and evaluation of simple order of operations 4'''
		self.assertEqual(infix_to_postfix("3 + 4 * 5"),"3 4 5 * +")
		self.assertEqual(postfix_eval("3 4 5 * +"),23)
		self.assertEqual(postfix_eval(infix_to_postfix("3 + 4 * 5")),23)

	def test_simple_ooo5(self):
		'''Tests conversion and evaluation of simple order of operations 5'''
		self.assertEqual(infix_to_postfix("3 + 4 * 5 - 6 - 6"),"3 4 5 * + 6 - 6 -")
		self.assertEqual(postfix_eval(infix_to_postfix("3 + 4 * 5 - 6 - 6")),11)

	def test_simple_ooo6(self):
		'''Tests conversion and evaluation of simple order of operations 6'''
		self.assertEqual(infix_to_postfix("( 3 + 4 ) * 5 )"),"3 4 + 5 *")
		self.assertEqual(postfix_eval(" 4 3 + 5 * "),35)
		self.assertEqual(postfix_eval(infix_to_postfix("( 3 + 4 ) * 5 )")),35)

	def test_simple_ooo7(self):
		'''Tests conversion and evaluation of simple order of operations 7'''
		self.assertEqual(infix_to_postfix("8 - ( 2 + 3 )"),"8 2 3 + -")
		self.assertEqual(postfix_eval(infix_to_postfix("8 - ( 2 + 3 )")),3)

	def test_harder_ooo1(self):
		'''Tests conversion and evaluation of more difficult order of operations 1'''
		self.assertEqual(postfix_eval("1 2 - 3 + 4 5 * +"),22)

	def test_difficult_ooo1(self):
		'''Tests conversion and evaluation of very difficult order of operations 1'''
		self.assertEqual(infix_to_postfix("2 ^ 8 - 6 / 3 * 2 + 2 ^ 3"),"2 8 ^ 6 3 / 2 * - 2 3 ^ +")
		self.assertEqual(postfix_eval(infix_to_postfix("2 ^ 8 - 6 / 3 * 2 + 2 ^ 3")),(2**8) - ((6/3) * 2) + (2**3))

	def test_difficult_ooo2(self):
		'''Tests conversion and evaluation of very difficult order of operations 2'''
		self.assertEqual(postfix_eval(infix_to_postfix("12 / 6 / 2 * 1 * 9 ^ 0 + 3")),(((12/6)/2) * 1 * (9**0)) + 3)

	def test_decimals1(self):
		self.assertEqual(postfix_eval(infix_to_postfix("3 * ( 0.2 + 0.3 ) * 2")),3)


if __name__ == "__main__":
	unittest.main()
