# https://leetcode.com/problems/move-zeroes/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# hahah , Here I come with my cheap python hacks ! Reminds me of this xkcd
# https://xkcd.com/353/
# Unlike other problems though , I dont understand if this was intented to be done a different way , probably do that remove by hand.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)


my_solution = Solution()
nums = [1,1,1,0,3,12]
nums_1 = [0,1,2,3,4,5]
my_solution.moveZeroes(nums)
my_solution.moveZeroes(nums_1)
