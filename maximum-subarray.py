class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        # this is best solved using Kadane's algorithm
        # we need two variables to solve this - 
        #  --- (1) max ending here - this keeps track of the largest subbarray sum till that particular index
        #  --- (2) max so far - this keeps track of the largest sum of all sub arrays parsed so far.
        max_ending_here = A[0]
        max_so_far      = A[0]
        # We initialize both of these variables to A[0] - the first element of the array.
        
        for x in A[1:]:
            #starting from the second element , A[1]
            max_ending_here = max(x, max_ending_here+x)
            max_so_far = max(max_so_far,max_ending_here)
            
        return max_so_far
        