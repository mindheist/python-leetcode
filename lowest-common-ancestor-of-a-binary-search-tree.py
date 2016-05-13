# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#

# solution video : https://www.youtube.com/watch?v=TIoCCStdiFo

# algorithm
# ========
# start with the root node
# if the root value is less than both the nodes , move to the right on the tree & recursively call the function
# if the root value is more than both the nodes , move to the left on the tree  & recursively call the function
# return root if none of these return anything
# Hmm .. I would love to prove this algorithm; I can see this works. But I m still struggling to see why it works
# I understand its the binary tree property that makes this work .

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val > max(p.val,q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < min(p.val,q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root.val
