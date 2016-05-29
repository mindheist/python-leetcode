#https://leetcode.com/problems/happy-number/

# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# the biggest trouble I had in solving this problem was finding how to exit the loop when you start looping endlessly
# this is solved using a lookup hash table.

import unittest
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {}
        while n!=1 and n not in lookup:
            lookup[n] = True
            n = map(int,str(n))
            n = sum([i*i for i in n])
        return n==1

class TestHappyNumber(unittest.TestCase):
    my_solution = Solution()

    def test_happy_number(self):
        self.assertTrue(self.my_solution.isHappy(82))

    def test_not_happy_number(self):
        self.assertFalse(self.my_solution.isHappy(45))

    def test_with_zero(self):
        self.assertFalse(self.my_solution.isHappy(0))

if __name__ == "__main__":
    unittest.main()
