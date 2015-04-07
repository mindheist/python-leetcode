# https://leetcode.com/problems/remove-element/
# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer

    #Solution
    #========
    # (1) Using List comprehentions / filtering here to exclude the "element"
    def removeElement(self, A, elem):
        A[:] = [element for element in A if element!=elem]
        return len(A)
        # Learn List filtering through this.