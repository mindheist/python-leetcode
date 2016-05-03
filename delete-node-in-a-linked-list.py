# https://leetcode.com/problems/delete-node-in-a-linked-list/
#
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

# I somehow feel this question in itself is a hack , and confuses people solving l33tcode puzzles.
#  Unlike other problems where you legimately solve it by switching around pointers , we resort to
# copying over data . Though it explicitly says , we dont have access to the previous node - I find this to be an underarm ball.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node_to_delete = node.next
            node.val = node_to_delete.val
            node.next = node_to_delete.next
            # del node_to_delete --> I see some people do this at the end of the solution
            # Never has leetcode mentioned the availability of 'del', should ponder into
            # this more
