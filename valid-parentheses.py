# https://leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

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