# problem : https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# For example,
# If n = 4 and k = 2, a solution is:


# Solution
# ========
# One of python's inbuilt function makes this problem much easier to solve (ie)
# itertools has a function of name combinations() ; given a list S and desired length of subset k --> it gives all possible output sets
# the same tools were used to solve the subsets problem : https://leetcode.com/problems/subsets/

import itertools
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return_list = []
        S = list(range(1,n+1))
        return_list.extend(list(x) for x in itertools.combinations(S,k))
        return return_list

