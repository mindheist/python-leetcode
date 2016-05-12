# https://leetcode.com/problems/add-digits/
#
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

# The use of python's inbuilt function map does the trick here
import unittest
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        my_sum = 0
        num = str(num)
        while len(num) > 1:
            num = map(int , num)
            num = sum(num)
            num = str(num)
        return int(num)

class TestAddDigits(unittest.TestCase):
    my_solution = Solution()

    def test_two_digit_number(self):
        self.assertEqual(self.my_solution.addDigits(15),6)


if __name__ == "__main__":
    unittest.main()


my_solution = Solution()
print my_solution.addDigits(157)
