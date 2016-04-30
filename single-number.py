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
            print nums
            for i in range(0,len(nums)-1,2):
                #print nums[i],nums[i+1],nums[i]==nums[i+1]
                if nums[i] == nums[i+1]:
                    pass
                else:
                    return nums[i]
            return nums[len(nums)-1]


my_solution = Solution()
print my_solution.singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])
print my_solution.singleNumber([1,1,2,2,3])
