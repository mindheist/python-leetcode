# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?

# This is a pretty basic solution ; not sure how I would do it without loops

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>1:
            while n%3==0:
                n = n/3
        return n==1
