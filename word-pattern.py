# https://leetcode.com/problems/word-pattern/

# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

# The idea here is to use a dictionary , mapping characters from the pattern to the words in the string

import unittest
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        else:
            my_dict = {}
            for i in xrange(len(pattern)):
                if pattern[i] not in my_dict:
                    if str.split()[i] in my_dict.values():
                        return False
                    else:
                        my_dict[pattern[i]] = str.split()[i]
                elif pattern[i] in my_dict:
                    #print pattern[i],my_dict[pattern[i]],str.split()[i]
                    if my_dict[pattern[i]] != str.split()[i]:
                        return False
                    else:
                        my_dict[pattern[i]] = str.split()[i]
            return True

class TestWordPattern(unittest.TestCase):

    my_solution = Solution()
    def test_default_pass(self):
        self.assertTrue(self.my_solution.wordPattern("abba","dog cat cat dog"))

    def test_default_fail(self):
        self.assertFalse(self.my_solution.wordPattern("abba","dog cat cat fish"))

    def test_default_fail(self):
        self.assertFalse(self.my_solution.wordPattern("aaaa","dog cat cat dog"))

    def test_default_fail(self):
        self.assertFalse(self.my_solution.wordPattern("abba","dog dog dog dog"))

    def test_not_a_pattern(self):
        self.assertFalse(self.my_solution.wordPattern("abba","dog cat cat sheep"))

    def test_empty_pattern(self):
        self.assertFalse(self.my_solution.wordPattern("","dog dog dog dog"))

    def test_empty_string(self):
        self.assertFalse(self.my_solution.wordPattern("abba",""))

    def test_empty_pattern_string(self):
        self.assertTrue(self.my_solution.wordPattern("",""))

    def test_pattern_longer_than_string(self):
        self.assertFalse(self.my_solution.wordPattern("abbba","cat dog dog dog"))

    def test_string_longer_than_pattern(self):
        self.assertFalse(self.my_solution.wordPattern("abba","cat dog"))

    def test_long_pattern_and_string_pass(self):
        self.assertTrue(self.my_solution.wordPattern("abcdefghijklmnopqrstuvwxyz","abbess abbey abbot abbreviate abbreviation abdicate abdomen abduct abeam abecedarian abed aberration abet abeyance abhor abhorrent abide ability abject abjure ablate ablative ablaze able abloom ablution"))

    def test_long_pattern_and_string_fail(self):
        self.assertFalse(self.my_solution.wordPattern("abcdefghijklmnopqrstuvwxy","abbess abbey abbot abbreviate abbreviation abdicate abdomen abduct abeam abecedarian abed aberration abet abeyance abhor abhorrent abide ability abject abjure ablate ablative ablaze able abloom ablution"))



if __name__ == '__main__':
    unittest.main()


#print my_solution.wordPattern("abba","dog cat cat sheep")
#print my_solution.wordPattern("abba","dog cat cat dog")
#print my_solution.wordPattern("abba","dog dog dog dog")
