# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# here is the video explanation of this : https://www.youtube.com/watch?v=MILxfAbIhrE

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sys_max , sys_min = float("inf"), float("-inf")
        return self.isBST(root,sys_min,sys_max)

    def isBST(self, root , min,max):
        if root is None :
            return True
        if min < root.val  or root.val < max:
            return False
        else:
            return self.isBST(root.left,min,root.val) and \
            self.isBST(root.right,root.val,max)
