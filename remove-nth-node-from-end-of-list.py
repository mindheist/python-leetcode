# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):

        fast_pointer = head
        slow_pointer = head
        
        for _ in range(n-1):
            fast_pointer = fast_pointer.next
            
        if fast_pointer.next == None:
            head = head.next
            
        else :
            
            fast_pointer = fast_pointer.next
            
            while fast_pointer.next != None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
                
            slow_pointer.next = slow_pointer.next.next
        
        return head