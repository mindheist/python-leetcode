# product-of-array-except-self
# sucessfully reduced the Time complexity from O(n^2) to O(n)
# still failing on three tests, 14/17 tests passed for the following solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = 1
        for i in xrange(len(nums)):
            result = result * nums[i]

        results_list = []

        for i in xrange(len(nums)):
            if nums[i]!=0:
                results_list.append(result/nums[i])
            else:
                results_list.append(result)
        return results_list

my_solution = Solution()
print my_solution.productExceptSelf([1,2,3,4,5])
#print my_solution.productExceptSelf([0])
