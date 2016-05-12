# https://leetcode.com/problems/power-of-two/

#  Given an integer, write a function to determine if it is a power of two.
#  For a number to be a power of 2 : it has to satisfy the following simple condition
#  It should result in a 0 if you AND the number n with n-1
#  If you think about this in the 8421 notation , its nothing but 2^0 , 2^1 , 2^2 , 2^3 , 2^4 etc., etc.,
#  And n always has exactly a single binary 1 set , and the rest of them are zeros
#  And n-1 flips all the remaining 1 bits ; ANDing them results in Zero

import unittest

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        else:
        #Step 1: Use the above explained logic here
            return (n & n-1)==0

class TestPowerOfTwo(unittest.TestCase):
    my_solution = Solution()

    def test_two_power_three(self):
        self.assertTrue(self.my_solution.isPowerOfTwo(8))

    def test_not_a_power_of_two(self):
        self.assertFalse(self.my_solution.isPowerOfTwo(1000))

    def test_for_zero(self):
        self.assertFalse(self.my_solution.isPowerOfTwo(0))

    def test_for_one(self):
        self.assertTrue(self.my_solution.isPowerOfTwo(1))

if __name__ == "__main__":
    unittest.main()
