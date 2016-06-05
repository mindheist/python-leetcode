class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 :
            return 0
        else:
            self.max_diff = 0
            for i in xrange(len(nums)-1):
                diff = abs(nums[i+1]-nums[i])
                print i,diff
                if diff > self.max_diff:
                    self.max_diff = diff
                    print self.max_diff
                else:
                    continue
            return self.max_diff

my_solution = Solution()
#print my_solution.maximumGap([100,3,2,1])
print my_solution.maximumGap([3,6,9,1])
