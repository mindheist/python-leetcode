# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
