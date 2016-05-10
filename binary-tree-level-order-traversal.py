# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Overall Algorithm
# -----------------
#

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        # take care of the base condition ; the input could be an empty tree
        if root is None :
            return []
        # the difference between DFS and BFS is that - we use a Queue in BFS ( instead of a stack in DFS)
        else:
            processing_queue , final_result = [root],[]
            # seed the queue above with root element

            # ** Note : This is a conceptual Queue , the head of the queue could be either on the left or the right
            # if the head of the queue is on the left - you dequeue by popping the element at index 0
            #                                        - you enqueue by appending to the right of the list
            while processing_queue:
                level_vals , length = [],len(processing_queue)
                for i in range(length):
                    node = processing_queue[0]
                    level_vals.append(node.val)
                    if node.left:
                        processing_queue.append(node.left)
                    if node.right:
                        processing_queue.append(node.right)
                    processing_queue.pop(0)
                final_result.append(level_vals)
            return final_result
