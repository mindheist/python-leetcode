# https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This ideas seems right, but this is still not a working solution.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB ==None:
            return None
        else:
            current_A , current_B = headA,headB
            count_A,count_B = 1,1
            while current_A.next:
                current_A = current_A.next
                count_A +=1

            while current_B.next:
                current_B = current_B.next
                count_B +=1

            current_A , current_B = headA,headB
            diff = abs(count_A - count_B)
            print count_A , count_B
            if count_A > count_B:
                for i in xrange(diff):
                    current_A = current_A.next
                while current_A.next and current_B.next:
                    if current_A == current_B:
                        return current_A
                    else:
                        current_A = current_A.next
                        current_B = current_B.next
                    return None
            elif count_B > count_A :
                for i in xrange(diff):
                    current_B = current_B.next
                while current_A.next and current_B.next:
                    if current_A == current_B:
                        return current_A
                    else:
                        current_A = current_A.next
                        current_B = current_B.next
                    return None
