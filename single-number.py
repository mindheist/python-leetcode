# https://leetcode.com/problems/single-number/
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# ********** NOTE *************************
# Looks like l33tcode is not testing for empty string ; follow up
# This implementation is O(nlogn) solution ; assuming I do a quick sort ( python's inbuilt sorting does somethign called TimSort)
# An XOR based solution would take O(n) time , should try that next


import unittest

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
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

class TestSingleNumber(unittest.TestCase):
    my_solution = Solution()

    def test_small_array_all_positive(self):
        self.assertEqual(self.my_solution.singleNumber([1,2,1,2,3]),3)

    def test_small_array_mixed(self):
        self.assertEqual(self.my_solution.singleNumber([-1,-2,-1,-2,-3]),-3)

    def test_array_of_length_one(self):
        self.assertEqual(self.my_solution.singleNumber([1]),1)

    def test_empty_array(self):
        self.assertEqual(self.my_solution.singleNumber([]),None)

if __name__ == "__main__":
    unittest.main()


#print my_solution.singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])
#print my_solution.singleNumber([1,1,2,2,3])
