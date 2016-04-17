# https://leetcode.com/problems/contains-duplicate/
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# has_key() vs in  : http://stackoverflow.com/questions/1323410/has-key-or-in
# If you had implement this solution using has_keys() and bumped into an error,thats
# because has_Keys() has been deprecated in newer versions of python , using "in" is more pythonic

# Solution
# Create a dictionary or map datastructure , keep adding the numbers into the dictionary, bail out when you hit a dupe

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


# COMPLEXITY
# Well, this takes a single pass of the nums list , the solution is O(n) but takes additional space for the dictionary
