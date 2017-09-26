import unittest
import lab1

class TestLab1(unittest.TestCase):

    def test_max_list(self):
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(lab1.max_list_iter(tlist),10)
        tlist = []
        with self.assertRaises(ValueError):  # magic - uses context manager
            lab1.max_list_iter(tlist)  

    def test_reverse_rec(self):
        self.assertEqual(lab1.reverse_rec("abcd"),"dcba")
        self.assertEqual(lab1.reverse_rec(""),"")
        
    def test_bin_search(self):
        #Testing a normal list 
        list_val =[10,12,21,34,56,79,999]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(56,low, high, list_val),4)
        #Testing negative numbers
        list_val = [-100,-90,-75,-60,-20,-5]
        low = 0 
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(-100, low, high, list_val),0)
        #Testing negative numbers with ZERO
        list_val = [-100, -90, -75, -60, -20, -5, 0]
        low = 0 
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(0, low, high, list_val),6)
        #Testing an empty list
        list_val = []
        low = 0 
        high = len(list_val)-1
        self.assertEqual(lab1.bin_search(21,low,high,list_val),None)
        #Testing when target is in lower half 
        list_val =[1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(2,low, high, list_val),1)
        #Testing when target is in upper half 
        list_val =[1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(9,low, high, list_val),6)
        #Testing when target is in the middle
        list_val =[1,2,3,4,7,8,9,10,11]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(7,low, high, list_val),4)
        #Testing when there are multiple targets 
        list_val =[1,2,2,2,2,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(2,low, high, list_val),5)
        #Testing when the target is not in the list
        list_val =[1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(11,low, high, list_val),None)
        #Testing when the low and high bounds are mixed
        list_val =[1,2,3,4,7,8,9,10]
        low = len(list_val)-1
        high = 0
        with self.assertRaises(ValueError):
            lab1.bin_search(1,low,high,list_val)
        #Testing when the target is in the beginning 
        list_val =[1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(1,low, high, list_val),0)
        #Testing when the target is in the end
        list_val =[1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(10,low, high, list_val),7)
        #Testing when the list is in decimal form
        list_val =[1.0,2.0,3.0,4.0,7.0,8.0,9.0,10.0]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(4,low, high, list_val),3)
        #Testing when the target is in decimal form
        list_val =[1.0,2.0,3.0,4.0,7.0,8.0,9.0,10.0]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(4.0,low, high, list_val),3)
        #Testing when the list is in negative decimal form
        list_val =[-10.0,-9.0,-8.0,-7.0]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(-7,low, high, list_val),3)
        
if __name__ == "__main__":
        unittest.main()

    
