# https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Check out this video for the full length explanation : https://www.youtube.com/watch?v=nzmtCFNae9k
# This turned out to be a lil more tricky than I expected,but the idea is to use a stack and popping them
# in a specific order . ( Will add more comments to this.)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return_list = []
        if root == None:
            return []
        else:
            my_stack = []
            while(True):
                if root!= None:
                    my_stack.append(root)
                    root = root.left
                else:
                    if len(my_stack)==0:
                        break
                    else:
                        root= my_stack.pop()
                        return_list.append(root.val)
                        root = root.right
            return return_list
