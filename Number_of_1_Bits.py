# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return bin(n)[2:].count('1')

# the idea here is to use the inbuilt bin function -> that return the binary value of a given decimal number & use python 'count'