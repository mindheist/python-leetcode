# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        """
        # Using a regular level order traversal (either by inverting the order or insertion) or using a stack
        # The solution implemented so far is a little hacked, I did a regular level order traversal and
        # reversed alternate entries in the list to f list

        #Step 1 : levelOrder traversal
        levelOrder_list = self.levelOrder(self.root)
        # Step 2 : Reverse the Level Order traversal
        for i in xrange(len(levelOrder_list)):
            if i%2 == 1:
                levelOrder_list[i] = levelOrder_list[i][::-1]
        return levelOrder_list

    def levelOrder(self,root):
        self.root = root
        if self.root == None:
            return []
        else:
            processing_queue , results = [self.root],[]
            while processing_queue:
                level_vals , length = [],len(processing_queue)
                for i in xrange(length):
                    temp_node = processing_queue[0]
                    level_vals.append(temp_node.val)
                    if temp_node.left:
                        processing_queue.append(temp_node.left)
                    if temp_node.right:
                        processing_queue.append(temp_node.right)
                    processing_queue.pop(0)
                results.append(level_vals)
            return results
