# https://leetcode.com/problems/two-sum/
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# UPDATE (2016/2/13):
# The return format had been changed to zero-based indices. Please read the above updated description carefully.

import unittest
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #print nums

        # step 1 : create a dictionary - add all elements of the dictionary into it , with the value as the key and index as the value :P :P

        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        #step 2 : if target - number is in the dictionary, return those indices . Please note an input like print my_solution.twoSum([3,2,4],6)
        # can break your logic , since adding the same number twice can yield the target.
        for i in range(len(nums)):
            #print "Iteration number",i
            if (target - nums[i]) in lookup and lookup[target - nums[i]] != i :
                return [i,lookup[target-nums[i]]]
        # step 3 : Return [] if no such pair is found.
        return []

class TestTwoSum(unittest.TestCase):
    my_solution = Solution()

    def test_default_pass(self):
        self.assertEquals(self.my_solution.twoSum([2, 7, 11, 15],9),[0,1])

if __name__ == "__main__":
    unittest.main()

# test_!
#print my_solution.twoSum([2, 7, 11, 15],9)
# print my_solution.twoSum([2, 7, 11, 15],26)
# print my_solution.twoSum([3,2,4],6)
# print my_solution.twoSum([3,2,4],8)
