class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
            else:
                continue
        return nums


my_solution = Solution()
print my_solution.removeDuplicates([1,2,2,3,4])
