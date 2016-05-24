# https://leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

# Solution video : https://www.youtube.com/watch?v=siKFOI8PNKM

import unittest
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        else:
            result = []
            type(result)

            rows = len(matrix)
            columns = len(matrix[0])

            top = 0
            bottom = rows

            left = 0
            right = columns

            print "top",top,"bottom",bottom,"left",left,"right",right
            direction = 0
            while (top < bottom and left <= right):
                if direction == 0:
                    for i in xrange(left,right):
                        result.append(matrix[top][i])
                    top = top +1
                    direction =1
                    print "1",result
                elif direction == 1:
                    for i in xrange(top,bottom):
                        result.append(matrix[i][right-1])
                    right = right -1
                    direction=2
                    print "2",result

                elif direction == 2 :
                    # right to left
                    for i in xrange(right-1,left-1,-1):
                        if top<bottom:
                            result.append(matrix[bottom-1][i])
                    bottom = bottom -1
                    direction = 3
                    print "3",result

                elif direction == 3 :
                    for i in xrange( bottom-1,top-1 ,-1):
                        if left<right:
                            result.append(matrix[i][left])
                    left = left + 1
                    direction =0
                    print "4",result
            return result

class TestSpiralMatrix(unittest.TestCase):
    my_solution = Solution()

    def test_all_zero_matrix_3X3_(self):
        self.assertEquals(self.my_solution.spiralOrder([[ 0, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 0 ]]),[0,0,0,0,0,0,0,0,0])

    def test_3_X_3_matrix(self):
        self.assertEquals(self.my_solution.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]),[1,2,3,6,9,8,7,4,5])

    def test_4_X_4_matrix(self):
        self.assertEquals(self.my_solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]),[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

    def test_1_X_2_matrix(self):
        self.assertEquals(self.my_solution.spiralOrder([[2,3]]),[2,3])

    def test_3_X_2_matrix(self):
        self.assertEquals(self.my_solution.spiralOrder([[2,5,8],[4,0,-1]]),[2,5,8,-1,0,4])

    def test_empty_matrix(self):
        self.assertEquals(self.my_solution.spiralOrder([]),[])

if __name__ == "__main__":
    unittest.main()
