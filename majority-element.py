# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2  times.
# You may assume that the array is non-empty and the majority element always exist in the array.



class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        return sorted(num)[len(num)/2]
        # This program uses the logic that , if a number appears more than n/2 times in the array - then the n/2-nd element
        # should be what we are looking for
        # 1. Sort the Array
        # 2. Return n/2th element