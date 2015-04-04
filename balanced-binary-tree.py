# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.





# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The expected result is to return a bool ; True -> if its balanced & False -> if not balanced

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return (self.getHeight(root) >=0 )
        
        
    def getHeight(self,root):
        if root is None:
            return 0
        left_height, right_height  = self.getHeight(root.left),self.getHeight(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height,right_height) + 1