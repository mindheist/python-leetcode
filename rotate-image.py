class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        matrix[:] = [list(element) for element in matrix ]