# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to num2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

import unittest
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        my_dict = dict()
        for i in xrange(len(nums1)):
            if nums1[i] not in my_dict:
                my_dict[nums1[i]] = 1
            else:
                my_dict[nums1[i]]+=1
        return_list = []
        for i in xrange(len(nums2)):
            if nums2[i] in my_dict and my_dict[nums2[i]]>0:
                return_list.append(nums2[i])
                my_dict[nums2[i]]-=1
            else:
                continue
        return return_list

class TestArrayIntersection(unittest.TestCase):
    my_solution = Solution()
    def test_no_duplicate_inputs(self):
        self.assertEqual(self.my_solution.intersect([1,2,3,4],[2,3,5,6]),[2,3])

    def test_with_duplicates(self):
        self.assertEqual(self.my_solution.intersect([1,1,2,3],[1,1]),[1,1])

    def test_with_empty_arrays(self):
        self.assertEqual(self.my_solution.intersect([],[]),[])

if __name__ == "__main__":
    unittest.main()
