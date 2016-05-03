# https://leetcode.com/problems/rotate-lis/
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # some initial thoughts ; k > greater than length of the linked list , we need to use modulo to get the final k
        # use two pointers , fast and slow
        # move fast pointer k times.
        # keep moving slow and fast one at a time
        # when fast.next is NULL ; make fast.next --> HEAD and slow.next to NULL
        # calculate lenghth of list
        self.head = head

        # Step 1 : calculate length of the list in this part by traversing it all the way to the end once
        n = 1
        if self.head == None:
            n = 0
        elif self.head.next == None:
            n = 1
        else:
            current = self.head
            while current and current.next:
                n = n + 1
                current = current.next


        current = self.head
        if self.head == None:
            return []
        elif self.head.next == None:
            return self.head
        else:
            #Step 2: two pointers fast and slow start at the head of the list
            fast_pointer , slow_pointer = self.head,self.head
            k = k % n
            # Step 3 : Advance the fast pointer k times into the list . Now when the fast pointer hits End of List , it would exactly be pointing at the node ( which will be the
            # end of the new list)
            for i in range(k):
                fast_pointer = fast_pointer.next

            # Step 4 : Advance both pointers till you hit End of List.
            while fast_pointer and fast_pointer.next:
                slow_pointer,fast_pointer = slow_pointer.next,fast_pointer.next
            # Step 5 : Once you hit the end , move around the pointers like below
            fast_pointer.next = self.head
            self.head = slow_pointer.next
            slow_pointer.next = None

            return self.head
