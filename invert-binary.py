# https://leetcode.com/problems/invert-binary-tree/
# convert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so fuck off.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The solution to this problem involves using a Queue

# Step1 : Create a Queue with enqueue , dequeue and isempty functionality. These will come handy while
# inverting the binary tree
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,key):
        self.key = key
        self.items.insert(0,key)

    def dequeue(self):
        return self.items.pop()

    def empty(self):
        return self.items

    def isempty(self):
        return len(self.items)==0

    def print_q(self):
        return self.items

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

# Step 2 : if the tree is not an empty tree , enqueue the root into the Queue

# Step 3 : dequeue an element from the Queue , swap its left and right children

# Step 4 : enqueue these children that you just swapped in the Queue , as long as they are not None

# Step 5 : dequeue the next node from the Queue and swap its children .. Keep going.


        if root is not None:
            my_queue = Queue()
            my_queue.enqueue(root)
            while not my_queue.isempty():
                node = my_queue.dequeue()
                node.left , node.right = node.right , node.left
                if node.left is not None:
                    my_queue.enqueue(node.left)
                if node.right is not None:
                    my_queue.enqueue(node.right)
        return root
