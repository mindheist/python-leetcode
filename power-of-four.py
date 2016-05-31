class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num
        if n>1:
            while n%4==0:
                n = n/4
        return n==1
