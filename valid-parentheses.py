# https://leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Solution
# ========
# The idea here is to
# (1) use a map (dictinary) which contains opening parentheses as key and closing parantheses as the value
# (2) use a stack & push all opening parentheses into it.
# (3) Everytime you encounter a closing parantheses , pop the stack and lookup the map , if there is match ; the parantheses are balanced
# (4) continue till all opening parantheses are popped

import unittest

class Solution:
    # @return a boolean
    def isValid(self, s):
    	stack = []
    	my_dict = { '(':')' , '[':']' , '{':'}' }
    	for charater in s:
    		if charater == '(' or charater =='[' or charater == '{':
    			stack.append(charater)
    		elif charater == ')' or charater == ']' or charater == '}':
				if len(stack) == 0 or charater != my_dict[stack.pop()]:
					return False
				else:
					pass
	return len(stack) == 0

class TestValidParenthesis(unittest.TestCase):
    my_solution = Solution()

    def test_square_brackets(self):
        self.assertTrue(self.my_solution.isValid('[]'))

    def test_curly_braces(self):
        self.assertTrue(self.my_solution.isValid('{}'))

    def test_regular_brackets(self):
        self.assertTrue(self.my_solution.isValid('()'))

    def test_all_three_brackets(self):
        self.assertTrue(self.my_solution.isValid('()[]{}'))

    def test_nested_brackets(self):
        self.assertTrue(self.my_solution.isValid('{[()]}'))

    def test_fail_scenario(self):
        self.assertFalse(self.my_solution.isValid('(){}['))

if __name__ == "__main__":
    unittest.main()
