# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        return_list = ListNode(0)
        while l1.next and l2.next:
            temp_value = carry + l1.val + l2.val
            if l2.val > 10:
                l2.val = l2.val % 10
                carry = l2.val / 10
            l1,l2,return_list = l1.next,l2.next,return_list.next
        return return_list
