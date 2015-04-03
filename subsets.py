# Given a set of distinct integers, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


# Solution
# ========
# One of python's inbuilt function makes this problem much easier to solve (ie)
# itertools has a function of name combinations() ; given a list S and desired length of subset k --> it gives all possible output sets
# the same tools were used to solve the combinations problem : https://leetcode.com/problems/combinations/

import itertools	
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
    	return_list = []
    	S = sorted(S)
    	for i in range(len(S)+1):
    		return_list.extend (list(x) for x in itertools.combinations(S,i))
    	return return_list