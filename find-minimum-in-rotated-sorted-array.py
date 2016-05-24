# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

import unittest
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        elif len(nums) == 1:
            return nums[0]
        else:
            for i in xrange(len(nums)-1):
                if nums[i] < nums[i+1]:
                    continue
                else:
                    return nums[i+1]
            return nums[0] # in case there is no rotation

class TestMinRotatedArray(unittest.TestCase):
    my_solution = Solution()

    def test_simple_input(self):
        self.assertEquals(self.my_solution.findMin([4,5,6,7,0,1,2]),0)

    def test_none_list(self):
        self.assertEquals(self.my_solution.findMin(None),None)

    def test_non_rotated_list(self):
        self.assertEquals(self.my_solution.findMin([1,2,3,4,5,6]),1)

if __name__ == "__main__":
    unittest.main()
