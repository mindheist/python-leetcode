class Solution(object):
    def odd_even(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        odd_pointer = self.head.next
        current , even_pointer = self.head

        for current and current.next.next :
            even_pointer.next = even_pointer.next.next
