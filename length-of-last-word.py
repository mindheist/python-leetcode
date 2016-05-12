# https://leetcode.com/problems/length-of-last-word/

# Given a string s consists of upper/lower-case alphabets and empty space characters return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example,
# Given s = "Hello World",
# return 5.

import unittest

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        string_list = s.split(' ')
        return len(string_list[len(string_list) - 1])

class TestLastWordLength(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("Hello World"),5)

    def test_leading_spaces_string(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("           Hey you world"),5)

    def test_trailing_spaces_string(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("Hiiiiiiii World               "),5)

    def test_uppercase_last_word(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("hello WORLD"),5)

    def test_empty_string(self):
        self.assertEqual(self.my_solution.lengthOfLastWord(""),0)

    def test_one_word_string(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("dkjhvalsjvhjkalvhgdslahkvacsdhksfashjkfnjdafsoyucigkhj;gudsioygkjhjldfsyuig"),75)

    def test_one_word_integer_string(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("6787676543456789876543456789"),28)

    def test_last_word_integer_string(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("helllo world 678767654345678987654345678990"),30)

    def test_one_word_special_charaters(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("$%Y$#$!%$@&%^$!%@#$#^%$&^*(&)*^$%$#@!#@^$&%*$%(&)^*_&(+_"),56)

    def test_last_word_special_characters(self):
        self.assertEqual(self.my_solution.lengthOfLastWord("hello World $%Y$#$!%$@&%^$!%@#$#^%$&^*(&)*^$%$#@!#@^$&%*$%(&)^*_&(+_$$##"),60)

if __name__ == "__main__":
    unittest.main()
