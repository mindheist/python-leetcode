class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        A = sorted(A + B )
        if len(A) > 2:
            if len(A)%2 != 0 :
                return A[(len(A)/2)]
            return float(A[(len(A)/2)] + A[(len(A)/2)-1])/2
        elif len(A) ==2 :
            return float(A[0] + A[1])/2
        elif len(A) == 1:
            return A[0]
        elif len(A) == 0:
            return None 