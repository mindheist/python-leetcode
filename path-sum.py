# https://leetcode.com/problems/path-sum/
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        elif root.left == None and root.right == None :
            return root.val == sum
        elif root.left == None:
            return self.hasPathSum(root.right , sum - root.val)
        elif root.right == None:
            return self.hasPathSum(root.left , sum - root.val)
        else:
            return self.hasPathSum(root.left,sum -root.val) or self.hasPathSum(root.right , sum - root.val)
