# https://leetcode.com/problems/contains-duplicate/

# hint : http://stackoverflow.com/questions/1323410/has-key-or-in
class Solution(object):
    def containsDuplicate(self, nums):
        self.my_dict={}
        self.nums = nums

        for i in range(len(self.nums)):
            #if self.my_dict.has_Key(self.nums[i]) == True:
            if self.nums[i] in self.my_dict:
                return True
            else:
                self.my_dict[nums[i]] = 0
        return False


# TESTING
my_solution = Solution()
numbers_test_1 = [3,5,7,8,9,23,12]
print my_solution.containsDuplicate(numbers_test_1)

numbers_test_2 = [3,5,7,8,9,23,12,3]
print my_solution.containsDuplicate(numbers_test_2)
