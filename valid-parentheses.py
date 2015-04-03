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