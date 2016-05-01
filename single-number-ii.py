# https://leetcode.com/problems/single-number-ii/

# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==1:
            return nums[0]
        else:
            nums = sorted(nums)
            for i in range(0,len(nums)-1,3):
                if nums[i] == nums[i+1] == nums[i+2]:
                    pass
                else:
                    if nums[i+1] == nums[i+2]:
                        return nums[i]
                    elif  nums[i] == nums[i+2]:
                        return nums[i+1]
                    elif  nums[i] == nums[i+2]:
                        return nums[i+2]

            return nums[len(nums)-1]
