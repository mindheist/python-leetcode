# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.

import unittest
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # invoking an advanced python-jutsu :P - I'll solve this by hand later
        return list(set(nums1) & set(nums2))

class TestIntersection(unittest.TestCase):
    my_solution = Solution()

    def test_simple_input(self):
        self.assertEquals(self.my_solution.intersection([1, 2, 2, 1],[2,2]),[2])

    def test_no_intersection_lists(self):
        self.assertEquals(self.my_solution.intersection([1,2,3,4,5,6,7],[8,9,0]),[])

    def test_one_empty_list(self):
        self.assertEquals(self.my_solution.intersection([1,2,3,4,5,6],[]),[])

    def test_both_empty_list_inputs(self):
        self.assertEquals(self.my_solution.intersection([],[]),[])

if __name__ == "__main__":
    unittest.main()
