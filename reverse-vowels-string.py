# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Subscribe to see which companies asked this question
import unittest
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None
        else:
            vowels = ['a','e','i','o','u','A','E','I','O','U']
            vowels_in_s = []
            for i in xrange(len(s)):
                if s[i] in vowels:
                    vowels_in_s.append(s[i])
                else:
                    continue
            s = list(s)
            for i in xrange(len(s)):
                if s[i] in vowels:
                    s[i] = vowels_in_s.pop()
                else:
                    continue
            return ''.join(s)

class TestReverseVowels(unittest.TestCase):
    my_solution = Solution()

    def test_simple_string(self):
        self.assertEquals(self.my_solution.reverseVowels("hello"),"holle")

    def test_capital_vowels(self):
        self.assertEquals(self.my_solution.reverseVowels("aA"),"Aa")

    def test_empty_string(self):
        self.assertEquals(self.my_solution.reverseVowels(""),"")

    def test_all_vowels_string(self):
        self.assertEquals(self.my_solution.reverseVowels("aeiouAEIOU"),"UOIEAuoiea")

    def test_no_vowels_string(self):
        self.assertEquals(self.my_solution.reverseVowels("bcdfghjklmnpqrstvwxyz"),"bcdfghjklmnpqrstvwxyz")

    def test_all_spaces_string(self):
        self.assertEquals(self.my_solution.reverseVowels("               "),"               ")

    def test_no_vowels_with_leading_spaces_string(self):
        self.assertEquals(self.my_solution.reverseVowels("    bcdfghjklmnpqrstvwxyz"),"    bcdfghjklmnpqrstvwxyz")

    def test_no_vowels_with_trailing_spaces_string(self):
        self.assertEquals(self.my_solution.reverseVowels("bcdfghjklmnpqrstvwxyz     "),"bcdfghjklmnpqrstvwxyz     ")

    def test_no_vowels_with_leading_and_trailing_spaces_string(self):
        self.assertEquals(self.my_solution.reverseVowels("    bcdfghjklmnpqrstvwxyz    "),"    bcdfghjklmnpqrstvwxyz    ")

    def test_all_vowels_with_leading_spaces(self):
        self.assertEquals(self.my_solution.reverseVowels("     aeiouAEIOU"),"     UOIEAuoiea")

    def test_all_vowels_with_trailing_spaces(self):
        self.assertEquals(self.my_solution.reverseVowels("aeiouAEIOU     "),"UOIEAuoiea     ")

    def test_all_vowels_with_leading_and_trailing_spaces(self):
        self.assertEquals(self.my_solution.reverseVowels("     aeiouAEIOU     "),"     UOIEAuoiea     ")

    def test_no_vowel_string_alphanumeric(self):
        self.assertEquals(self.my_solution.reverseVowels("123456789765432123456789"),"123456789765432123456789")

    def test_no_vowels_special_characters(self):
        self.assertEquals(self.my_solution.reverseVowels("!@#$%^&*(*&^%$#@#$%^%$#@"),"!@#$%^&*(*&^%$#@#$%^%$#@")

if __name__ == "__main__":
    unittest.main()
