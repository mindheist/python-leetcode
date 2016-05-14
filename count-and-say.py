# https://leetcode.com/problems/count-and-say/
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.

import unittest

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return 0
        seed = 1
        if n == 1:
            return "1"
        else:
            for i in xrange(n-1):
                seed = self.do_seq(seed)
            return seed


    def do_seq(self,seed):
        seed = str(seed)
        if seed is None:
            return None
        elif len(seed)==1:
            return str(1)+seed[0]
        else:
            count = 1
            return_string = ""
            for i in xrange(len(seed)-1):
                if seed[i] == seed[i+1]:
                    count = count + 1
                else:
                    return_string = return_string + str(count) + seed[i]
                    count = 1
            return_string = return_string  + str(count)+ seed[i+1]
            return return_string

class TestCountAndSay(unittest.TestCase):
    my_solution = Solution()

    def test_n_equal_1(self):
        self.assertEquals(self.my_solution.countAndSay(1),"1")

    def test_n_equal_2(self):
        self.assertEquals(self.my_solution.countAndSay(2),"11")

    def test_n_equal_3(self):
        self.assertEquals(self.my_solution.countAndSay(3),"21")

    def test_n_equal_4(self):
        self.assertEquals(self.my_solution.countAndSay(4),"1211")

    def test_n_is_None(self):
        self.assertEquals(self.my_solution.countAndSay(0),0)

if __name__ == "__main__":
    unittest.main()
