# https://leetcode.com/problems/power-of-four/
#
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?
#
# Not sure how i would do this without loops
import unittest

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num
        if n>1:
            while n%4==0:
                n = n/4
        return n==1

class TestPowerOfFour(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertTrue(self.my_solution.isPowerOfFour(16))

    def test_default_fail(self):
        self.assertFalse(self.my_solution.isPowerOfFour(40))

    def test_for_zero(self):
        self.assertFalse(self.my_solution.isPowerOfFour(0))
        # Should 0 return True or False ?

if __name__ == "__main__":
    unittest.main()
