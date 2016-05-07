# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# peope always use height and depth interchangeably : This article explains the difference clearly

# http://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height

# should add visualization to this recursive solution.


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None :
            return 0
        return 1 + max ( self.maxDepth(root.left),self.maxDepth(root.right))
