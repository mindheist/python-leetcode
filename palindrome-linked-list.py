# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# I think I should implement the stack solution here as well , using [::-1] *might* be cheating
# its a construct that is not available in other languages , so ..

class Solution_1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        current = head
        if head == None :
           return True
        else:
            while current:
                result.append(str(current.val))
                current = current.next
        return result == result[::-1]


# A simple solution is to use a stack of list nodes. This mainly involves three steps.
# 1) Traverse the given list from head to tail and push every visited node to stack.
# 2) Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
# 3) If all nodes matched, then return true, else false.

import unittest
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.head = head
        current = self.head
        my_stack = []

        if self.head is None:
            return True
        elif self.head.next is None:
            return True
        else:

            while current.next:
                my_stack.append(current.val)
                current = current.next
            my_stack.append(current.val)
            #print my_stack

            current = self.head
            # print current.val
            while current.next:
                if current.val == my_stack.pop():
                    current = current.next
                else:
                    return False
            return True

class TestPalindromeLinkedList(unittest.TestCase):
    my_solution = Solution()

    def test_not_a_palindrome(self):
        A,B,C,D,E = ListNode("A"),ListNode("B"),ListNode("C"),ListNode("D"),ListNode("E")
        A.next = B
        B.next = C
        C.next = D
        D.next = E
        self.assertFalse(self.my_solution.isPalindrome(A))

    def test_is_a_palindrome(self):
        A,B,C,D,E = ListNode("R"),ListNode("A"),ListNode("D"),ListNode("A"),ListNode("R")
        A.next = B
        B.next = C
        C.next = D
        D.next = E
        self.assertTrue(self.my_solution.isPalindrome(A))

if __name__ == "__main__":
    unittest.main()
