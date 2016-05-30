class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.my_dict = {-1:0}
        for i,v in enumerate(self.nums):
            self.my_dict[i] = self.my_dict[i-1] + v


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.my_dict[j]-self.my_dict[i-1]


class SolutionRangeSum(unittest.TestCase):
    my_solution = Solution()

    # must add tests here
