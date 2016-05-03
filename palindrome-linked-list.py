# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# I think I should implement the stack solution here as well , using [::-1] *might* be cheating
# its a construct that is not available in other languages , so .. 

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        current = head
        if head == None :
           return True
        else:
            while current:
                result.append(str(current.val))
                current = current.next
        return result == result[::-1]
