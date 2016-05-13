# https://leetcode.com/problems/reverse-integer/

#Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321
#  Looks like l33tcode has this solution implemented for Java/ C , Note that
# the system max in those languages have a different range

# Thinking about this again , I guess I might have taken a short cut here .
# I shouldn't have used string reverse here , and should have used a multiply logic.

import unittest
import sys
import math
class Solution:
    # @return an integer
    def reverse(self, x):
    	isNegative = False
    	new_sysmax = int(math.pow(2,31)-1)
    	new_sysmin = new_sysmax*-1
    	if x < 0 :
    		rev_int = int(str(abs(x))[::-1])*-1
    		if rev_int < new_sysmin:
    		    return 0
    		else:
    		    return rev_int
    	else:
    	    rev_int = int(str(abs(x))[::-1])
    	    if rev_int < new_sysmax:
    	        return rev_int
    	    else:
    	        return 0

class TestReverseInteger(unittest.TestCase):
    my_solution = Solution()

    def test_reverse_positive_integer(self):
        self.assertEqual(self.my_solution.reverse(123),321)

    def test_reverse_negative_integer(self):
        self.assertEqual(self.my_solution.reverse(-123),-321)

    def test_reverse_zero(self):
        self.assertEqual(self.my_solution.reverse(0),0)

    def test_overflow_max(self):
        self.assertEqual(self.my_solution.reverse(9463847412),0)
        # the reversed interger overflows the Maximum




if __name__ == "__main__":
    unittest.main()
