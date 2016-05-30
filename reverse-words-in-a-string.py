# amazon , lab126
import unittest
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # Step 1 : split the given string into a list of words - with " " as the seperator
        s = s.split(" ")
        # Step 2 : filter out the white spaces in the list and reverse the list
        s = [element for element in s if element != ''][::-1]
        # Step 3 : join them and return
        return ' '.join(s)

class Test_Reverse_Words_in_a_string(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertEqual(self.my_solution.reverseWords('Hello World'),'World Hello')

    def test_empty_string(self):
        self.assertEqual(self.my_solution.reverseWords(''),'')

    def test_one_word_string(self):
        self.assertEqual(self.my_solution.reverseWords('Hello'),'Hello')

if __name__ == "__main__":
    unittest.main()
