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

import unittest
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

class TestPascalsTriangle(unittest.TestCase):
    my_solution = Solution()

    def test_pascals_triangle_1(self):
        self.assertEqual(self.my_solution.generate(1),[[1]])

    def test_pascals_triangle_2(self):
        self.assertEqual(self.my_solution.generate(2),[[1], [1, 1]])

    def test_pascals_triangle_3(self):
        self.assertEqual(self.my_solution.generate(3),[[1], [1, 1], [1, 2, 1]])

    def test_pascals_triangle_4(self):
        self.assertEqual(self.my_solution.generate(4),[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_pascals_triangle_5(self):
        self.assertEqual(self.my_solution.generate(5),[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

if __name__ == "__main__":
    unittest.main()

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# my_solution = Solution()
# print my_solution.generate(6)
