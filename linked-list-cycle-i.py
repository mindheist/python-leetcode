# https://leetcode.com/problems/linked-list-cycle/

# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# the solution to the loop detecting problem is to use the popular floyd's algorithm which uses a slow and fast pointer.
# move the slow pointer by 1 and fast pointer by 2 : if they coincide - there exists a loop in the linked list
# if not ,the linked list doesnt have a loop

# but I still dont clearly understand the insight here, there are proofs that explain why this works. I should invest more
# time in understanding as to why this algorithm works - Why can you not increment the fast pointer by 5 & slow pointer by 3 and
# expect to detect a loop . Floyd's proof includes a detailed explaination of this insight . Infact , the actual beauty of this algorithm
# is the fact that he discovered is 2X relationship !!

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Step 1 : Initiate two pointers slow and fast and point them to the head of the linked list
        fast,slow = head,head
        while fast and fast.next:
        # Step 2 : Increment fast pointer by 2 , slow by 1
            fast,slow = fast.next.next , slow.next
        # Step 3 : for every increment of the two pointers , check if the fast & slow pointers now point to the same node.
            if fast is slow:
        # Step 4 : Finally when they meet, it concludes the presence of a loop, return True
                return True
        # When the While loop breaks , it means there was no fast.next (or) in other words , we bumped into the end of the list and hence there is no cycle in the list
        return False
