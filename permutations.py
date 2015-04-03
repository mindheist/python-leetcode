# https://leetcode.com/problems/permutations/

#Given a collection of numbers, return all possible permutations.

#For example,
#[1,2,3] have the following permutations:
#[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

# Solution
# ========
# One of python's inbuilt function makes this problem much easier to solve (ie)
# itertools has a function of name permutations() ; given a list S and desired length of subsets it gives all possible permutations 
# a similar function was used to solve the combinations problem : https://leetcode.com/problems/combinations/ and the subset problem

# I m begining to think that I should re-solve this by hand without using itertools.


import itertools
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        length_num = len(num)
        return ([list(x) for x in itertools.permutations(num,length_num)])