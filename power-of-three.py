# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?

# This is a pretty basic solution ; not sure how I would do it without loops


import unittest
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>1:
            while n%3==0:
                n = n/3
        return n==1

class TestPowerofThree(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertTrue(self.my_solution.isPowerOfThree(27))

    def test_default_fail(self):
        self.assertFalse(self.my_solution.isPowerOfThree(30))

if __name__ == "__main__":
    unittest.main()
