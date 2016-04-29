# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# We once again use a fast and slow pointer approach to this problem

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):

        #Step 1 : Initiate two pointers fast and slow and point them to the head of the list

        fast_pointer = head
        slow_pointer = head
        # Step 2 : Move the fast pointer to n-1 places into the list. Please note range(2) gives 0,1 : range(3) is 0,1,2
        # So , we are infact moving n counts , though it says n-1 as the range parameter
        for _ in range(n-1):
            fast_pointer = fast_pointer.next
        # Step 3 : After you are done moving the fast pointer n-1 places into the list , we might have reached the end of the list
        # Assume the list has 5 nodes , and we are attempting to remove the 5th element from the last , which is nothing but the head
        # So we move the head one step into the list
        if fast_pointer.next == None:
            head = head.next

        else :
        # Step 4 : Move the fast pointer one node forward if the above statement wasn't true
            fast_pointer = fast_pointer.next
        # Step 5: Continue to move the slow point and the fast pointer one by one. When you hit the end of the list , you stop just one short of the
        # node to be deleted.
            while fast_pointer.next != None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
        # step 6: redirect the link of the slow pointer OVER the node to be deleted ! Mission Accomplished !!
            slow_pointer.next = slow_pointer.next.next
        return head
