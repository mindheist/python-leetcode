# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        # solve the base case first (ie) if the root was null
        if root is None:
            return []
        # so, once again the output expected is a list of list (but in the reverse order)
        # we need two variables here queue[] 
        queue = [root] # seed the queue with the root of the tree
        result = []
        while queue:
            length = len(queue)
            level  = []
            for i in range(length):
                node = queue[0]             # take the first element out of the queue
                level.append(node.val)    # take the value of the node and copy it to level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queue.pop(0)
            result.append(level)
        return result[::-1]