#pascals-triangle-ii
# https://leetcode.com/problems/pascals-triangle-ii/
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
import unittest
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

class TestPascalsTriangle(unittest.TestCase):
    my_solution = Solution()

    # def test_pascals_triangle_1(self):
    #     self.assertEqual(self.my_solution.getRow(1),[1])

    def test_pascals_triangle_1(self):
        self.assertEqual(self.my_solution.getRow(1),[1, 1])

    def test_pascals_triangle_2(self):
        self.assertEqual(self.my_solution.getRow(2),[1, 2, 1])

    def test_pascals_triangle_3(self):
        self.assertEqual(self.my_solution.getRow(3),[1, 3, 3, 1])

    def test_pascals_triangle_4(self):
        self.assertEqual(self.my_solution.getRow(4),[1, 4, 6, 4, 1])

if __name__ == "__main__":
    unittest.main()
