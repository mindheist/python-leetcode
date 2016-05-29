# https://leetcode.com/problems/pascals-triangle/
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# solution video : https://www.youtube.com/watch?v=rlKGgxck7X0


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return_list = []
        ns = xrange(numRows)
        for n in ns:
            nlist = []
            for k in xrange(n+1):
                nlist.append(self.nchoosek(n,k))
            return_list.append(nlist)
        return return_list

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
print my_solution.generate(5)
