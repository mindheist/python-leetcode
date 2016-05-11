# https://leetcode.com/problems/number-of-1-bits/

# Write a function that takes an unsigned integer and returns the number of 1 bits it has (also known as the Hamming weight).

# For example, the 32-bit integer 11 has binary representation 00000000000000000000000000001011, so the function should return 3.

# @param n, an integer
# @return an integer
def hammingWeight(self, n):
    return bin(n)[2:].count('1')
# the idea here is to use the inbuilt bin function -> that return the binary value of a given decimal number & use python 'count'
