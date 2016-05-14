# https://leetcode.com/problems/top-k-frequent-elements/
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#

# I m guessing I might be using too many inbuild functions
# In a way ,thats the power of python - but I'll come back and implement some of the inbuilt functions
# used here


from collections import Counter
import unittest

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        return_list = []
        my_list = Counter(nums).most_common(k)
        for i in xrange(k):
            return_list.append(my_list[i][0])
        return return_list

class TestTopkFrequent(unittest.TestCase):
    my_solution = Solution()

    def test_k_equals_0(self):
        nums = [2,2,2,2,1,1,1,1,1,1,1,1,1,1,3,3]
        self.assertEquals(self.my_solution.topKFrequent(nums,0),[])

    def test_k_equals_1(self):
        nums = [2,2,2,2,1,1,1,1,1,1,1,1,1,1,3,3]
        self.assertEquals(self.my_solution.topKFrequent(nums,1),[1])

    def test_k_equals_2(self):
        nums = [2,2,2,2,1,1,1,1,1,1,1,1,1,1,3,3]
        self.assertEquals(self.my_solution.topKFrequent(nums,2),[1,2])

    def test_k_equals_3(self):
        nums = [2,2,2,2,1,1,1,1,1,1,1,1,1,1,3,3]
        self.assertEquals(self.my_solution.topKFrequent(nums,3),[1,2,3])






if __name__ == "__main__":
    unittest.main()
