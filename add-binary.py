# https://leetcode.com/problems/add-binary/

# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# # Solution
# ===========

# a and b are converted to int , added and the Solution is converted back to binary
# I guess I should revisit this and solve it without converting it back to decimal

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int (a,2) + int (b,2))[2:]