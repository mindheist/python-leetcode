# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Ah! for some reason, I took a really long time to wrap my head around this solution
# video explanation at : https://www.youtube.com/watch?v=PJzgqT2Ujek

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        self.head = head
        current = self.head
        previous = None
        next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        return self.head
