# https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetricHelper(self,left,right):
	    if left == None and right == None :
	    	return True
	    elif left == None or right == None :
	    	return False
	    elif left.val != right.val :
	    	return False
	    else :
	    	return self.isSymmetricHelper(left.right , right.left) and self.isSymmetricHelper(left.left,right.right)

    def isSymmetric(self, root):
    	if root == None : return True
    	else:
    		return self.isSymmetricHelper(root.left,root.right)
