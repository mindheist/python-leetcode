# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#
# Subscribe to see which companies asked this question

import unittest
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

class TestIsPalindrome(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertTrue(self.my_solution.isPalindrome(121))

    def test_not_a_palindrome(self):
        self.assertFalse(self.my_solution.isPalindrome(123143))

    def test_for_zero(self):
        self.assertTrue(self.my_solution.isPalindrome(0))


if __name__ == "__main__":
    unittest.main()

# Just realized , I converted the integer to a string , so - I suppose this is not a valid solution in that case
