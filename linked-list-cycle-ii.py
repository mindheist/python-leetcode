# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# this solution builds on the previos problem of finding a cycle in a linked list .
# As I already mentioned , I still dont completely understand the intuition behind this, in fact I now need to understand another extension

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Step 1 : Initiate two pointers slow and fast and point them to the head of the linked list
        fast,slow = head , head
        while fast and fast.next:
        # Step 2 : Increment fast pointer by 2 , slow by 1
            fast,slow = fast.next.next , slow.next
        # Step 3 : for every increment of the two pointers , check if the fast & slow pointers now point to the same node.
            if fast is slow:
        # Step 4 : Finally when they meet, it concludes the presence of a loop,but unlike the previous problem - its not sufficient to have just detected the loop
        # we also need to find where the loop begins.

        # Step 5 : Once we detect the existence of a loop , we reset the slow pointer back to the head
                slow = head
                while fast is not slow:
        # Step 6 : We now move both slow and fast pointer by 1 till they meet again
                    fast,slow = fast.next ,slow.next
        # Step 7 : The point they meet gives the 'beginning of the cycle'
                return fast  # Could return fast or slow pointer since they point to the same here.
        return None
