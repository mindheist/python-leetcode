# https://leetcode.com/problems/rotate-image/
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        matrix[:] = [list(element) for element in matrix ]
