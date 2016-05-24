# https://leetcode.com/problems/isomorphic-strings/
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

import unittest
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        else:
            list_s = list(s)
            list_t = list(t)
            my_dict = {}
            for i in xrange(len(s)):
                if list_s[i] in my_dict:
                    if my_dict[list_s[i]] == list_t[i]:
                        continue
                    else:
                        return False
                else:
                    my_dict[list_s[i]] = list_t[i]
            if len(set(my_dict.values()))<len(my_dict.keys()):
                return False
            else:
                return True

class TestIsomorphic(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertTrue(self.my_solution.isIsomorphic("add","egg"))

    def test_5_character_pass(self):
        self.assertTrue(self.my_solution.isIsomorphic("paper","title"))

    def test_default_fail(self):
        self.assertFalse(self.my_solution.isIsomorphic("foo","bar"))

    def test_aa_ab(self):
        self.assertFalse(self.my_solution.isIsomorphic("aa","ab"))
        # The check in line 39 was written to catch this failure

    def test_ab_aa(self):
        self.assertFalse(self.my_solution.isIsomorphic("ab","aa"))



if __name__ == "__main__":
    unittest.main()

my_solution = Solution()
# print my_solution.isIsomorphic("add","egg")
# print my_solution.isIsomorphic("Hello","World")
# print my_solution.isIsomorphic("paper","title")
print my_solution.isIsomorphic("ab","aa")
