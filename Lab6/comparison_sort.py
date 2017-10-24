import unittest
from comparison_sort import *
from random import randint
class countit():
	def __init__(self):
		self.num = 0
	def inc(self):
		self.num +=1
	def get(self):
		return self.num

def insert_sort(alist):
	"""Sorts a List by Insertion"""
	counter1 = countit()
	counter1.num= 0

	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index


		while position>0 and increment(currentvalue,alist[position-1],counter1):
			alist[position]=alist[position-1]
			position = position-1


		alist[position]=currentvalue
	return counter1.get()


def select_sort(alist):
	"""Sorts a List by Selection"""
	counter1 = countit()
	counter1.num= 0
	for fillslot in range(len(alist)-1,0,-1):
	   positionOfMax=0
	   for location in range(1,fillslot+1):
		   if increment(alist[positionOfMax],alist[location],counter1):
			   positionOfMax = location

	   temp = alist[fillslot]
	   alist[fillslot] = alist[positionOfMax]
	   alist[positionOfMax] = temp
	return counter1.get()
def merge_sort(alist,counter1=None):
	"""Sorts a List by Merging"""
	if counter1 is None:
		counter1 = countit()
		counter1.num = 0
	if len(alist) >= 2:
		first = alist[:(len(alist)//2)]
		last = alist[(len(alist)//2):]
		merge_sort(first,counter1)
		merge_sort(last,counter1)
		big = 0
		fi = 0
		li = 0
		while big < len(alist):
			if fi >= len(first) or ((not li >= len(last)) and increment(last[li],first[fi],counter1)):
				alist[big] = last[li]
				big += 1
				li += 1
			else:
				alist[big] = first[fi]
				big += 1
				fi += 1
	return counter1.get()
def increment(low,high,counter):
	counter.inc()
	return low < high
alist = list(range(50,0,-1))
print insert_sort(alist)
blist = list(range(50,0,-1))
print select_sort(blist)
clist = list(range(50,0,-1))
print merge_sort(clist)
class testing_sorts(unittest.TestCase):

	def test_worstcase_select(self):
		'''Any case is the worst case with selection sort--
		it will compare every element aganst each other every time'''
		l = [1,4,5,1,2,1,3,23,2,1]
		ssort = l[:]
		select_sort(ssort)
		pysort = l[:]
		'''Will go through outer loop n times
		Each time through outer loop will compare alist[big] to succeding elements:
		First time through outer loop: n-1 comparisons
		Second time: n-2 comparisons
		On (n-1)st pass, 1 comparison
		1 + 2 + ... + (n-2) + (n-1)
		= (n(n-1)) / 2 --> BigO(n^2)
		'''
		pysort.sort()
		self.assertEqual(ssort,pysort)

	def test_worstcase_insert(self):
		'''Worst case for insertion sort-- reverse order
		Effectively acts like selection sort by needing to compare every element against each other'''
		l = [9,8,7,6,5,4,3,2,1]
		isort = l[:]
		insert_sort(isort)
		pysort = l[:]
		'''Will loop through all indecies of the list
		On each execution of the loop, will decide where current element goes in the sorted preceeding spots
		In worst case, will have to compare with every element in sorted section of the list
			because the current element will always be lesser than its preceeding elements.
		First time: compare to the 1 sorted element = 1 comparison
		Second time: compare to the 2 sorted elements = 2
		= 1 + 2 + ... + (n-1)
		= (n(n-1)) / 2 --> BigO(n^2)
		'''
		pysort.sort()
		self.assertEqual(isort,pysort)

	def test_select(self):
		# insert_sort(None)
		# select_sort(None)
		# merge_sort(None)
		# pass
		l = [3,2,5,1,6,4]
		ssort = l[:]
		select_sort(ssort)
		pysort = l[:]
		pysort.sort()
		self.assertEqual(ssort,pysort)

	def test_insert(self):
		# insert_sort(None)
		# select_sort(None)
		# merge_sort(None)
		# pass
		l = [3,2,5,1,6,4]
		isort = l[:]
		insert_sort(isort)
		pysort = l[:]
		pysort.sort()
		self.assertEqual(isort,pysort)

	def test_merge(self):
		# insert_sort(None)
		# select_sort(None)
		# merge_sort(None)
		# pass
		l = [3,2,5,1,6,4]
		msort = l[:]
		merge_sort(msort)
		pysort = l[:]
		pysort.sort()
		self.assertEqual(msort,pysort)

	def test_select_random(self):
		for x in range(1):
			orig = []
			for y in range(randint(0,1000)):
				orig.append(randint(0,10000))
			tsort = orig[:]
			psort = orig[:]
			select_sort(tsort)
			psort.sort()
			self.assertEqual(tsort,psort)

	def test_insert_random(self):
		for x in range(1):
			orig = []
			for y in range(randint(0,1000)):
				orig.append(randint(0,10000))
			tsort = orig[:]
			psort = orig[:]
			insert_sort(tsort)
			psort.sort()
			self.assertEqual(tsort,psort)

	def test_merge_random(self):
		for x in range(1):
			orig = []
			for y in range(randint(0,1000)):
				orig.append(randint(0,10000))
			tsort = orig[:]
			psort = orig[:]
			merge_sort(tsort)
			psort.sort()
			self.assertEqual(len(tsort), len(psort))
			self.assertEqual(tsort,psort)






if __name__ == "__main__":
	unittest.main()
