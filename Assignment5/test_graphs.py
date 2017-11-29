import unittest
from my_graph import MyGraph

class testing_heaps(unittest.TestCase):

	def test_given_1_buildsize(self):
		mg = MyGraph('i1.txt')
		self.assertEqual(len(mg.adjlist),9)
		for i in range(len(mg.adjlist)):
			self.assertEqual(mg.adjlist[i][0],i+1)

	def test_give_2_adjlist(self):
		mg = MyGraph('i2.txt')

		expectation = [(1, [2, 3]), (2, [1, 3]), (3, [2, 1]), (4, [6, 7, 8]), (5, []), (6, [4]), (7, [4]), (8, [4])]
		for i in range(len(expectation)):
			self.assertEqual(expectation[i][0],mg.adjlist[i][0])
		for i in range(len(expectation)):
			self.assertEqual(expectation[i][0],mg.adjlist[i][0])
			es = sorted(expectation[i][1])
			ms = sorted(mg.adjlist[i][1])
			self.assertListEqual(es,ms)

	def test_give_1_adjlist(self):
		mg = MyGraph('i1.txt')

		expectation = [(1, [2,3,4,5]), (2, [1]), (3, [1]), (4, [1]), (5, [1]), (6, [7,8]), (7, [6,9]), (8, [6,9]), (9,[7,8])]
		for i in range(len(expectation)):
			self.assertEqual(expectation[i][0],mg.adjlist[i][0])
		for i in range(len(expectation)):
			self.assertEqual(expectation[i][0],mg.adjlist[i][0])
			es = sorted(expectation[i][1])
			ms = sorted(mg.adjlist[i][1])
			self.assertListEqual(es,ms)


	def test_given_1_cc(self):
		mg = MyGraph('i1.txt')
		self.assertListEqual(mg.conn_components(),[[1,2,3,4,5],[6,7,8,9]])
	def test_given_2_cc(self):
		mg = MyGraph('i2.txt')
		self.assertListEqual(mg.conn_components(),[[1,2,3],[4,6,7,8],[5]])

		
	# def test_given_1_bic(self):
	# 	mg = MyGraph('i1.txt')
	# 	self.assertTrue(mg.bicolor())
	# def test_given_2_bic(self):
	# 	mg = MyGraph('i2.txt')
	# 	self.assertFalse(mg.bicolor())


if __name__ == "__main__":
	unittest.main()

	
