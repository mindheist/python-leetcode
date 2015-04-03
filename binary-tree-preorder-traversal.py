# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Given a binary tree, return the preorder traversal of its nodes values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Solution
# ========

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        # the overall idea of a pre-order traversal is 
        # visit < root  >  node
        # visit < left  >  node 
        # visit < right >  node
        
        if root == None:
            return []
        
        # This problem is best solved using a stack to keep track of the nodes in a certain order
        stack =[] 
        stack.append(root)
        result = []
        
        while len(stack) != 0:
            current = stack.pop()
            result.append(current.val)
            if current.right != None :
                stack.append(current.right)
            if current.left  != None :
                stack.append(current.left)
            
        return result