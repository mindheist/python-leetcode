#pascals-triangle-ii
# https://leetcode.com/problems/pascals-triangle-ii/
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nlist = []
        n = rowIndex
        for k in xrange(n+1):
            nlist.append(self.nchoosek(n,k))
        return nlist

    def nchoosek(self,n,k):
        if k == 0 or k == n :
            return 1
        else:
            return self.factorial(n)/(self.factorial(k) * self.factorial(n-k))

    def factorial(self,n):
        if n==0:
            return 1
        else:
            return n*self.factorial(n-1)

my_solution = Solution()
print my_solution.getRow(5)
