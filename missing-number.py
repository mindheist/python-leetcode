# try the xor Solution from here http://www.geeksforgeeks.org/find-the-missing-number/

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        for i in xrange(len(nums)):
            result = result + nums[i]
        #print result

        n = len(nums)
        expected_result = n * ( n+1)/2
        return expected_result - result

my_solution = Solution()
print my_solution.missingNumber([0,1,2,4])
