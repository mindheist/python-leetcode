# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
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
# We use TWO QUEUES to perform a level order traversal on a Binary Tree - Call them processing_queue and final_queue
# Seed the processing_queue with the root of the tree
# Note that , in every iternation - the length and level_vals variables get reset
# We add the children of all nodes on the current level to the processing_queue and add all nodes in the current level to level_vals
# We keep appending the level_vals sublist to a final list and return it eventually
# Return an inverted list !! ( I m guessing this might be some kind of hack as well, may be I should rethink this.)

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        # solve the base case first (ie) if the root was null
        if root is None:
            return []
        # so, once again the output expected is a list of list (but in the reverse order)
        # we need two variables here queue[]
        else:
            processing_queue = [root] # seed the queue with the root of the tree
            result = []
            while processing_queue:
                length = len(processing_queue)
                level_vals  = []
                for i in range(length):

                    # *********************** Note ***********************
                    # This is a conceptual Queue , the head of the queue could be either on the left or the right hand side
                    # if the head of the queue is on the left - you dequeue by popping the element at index 0
                    #                                        - you enqueue by appending to the right of the list

                    # if the head of the Queue is assumed to be on the right - you enqueue by inserting at index 0
                    #                                                        - you dequeue by popping the element on index(length of the list)
                    # For our purposes , we are assuming the head is one the left ( first option above)
                    #*********************** Note ***********************
                    node = processing_queue[0]           # take the first element out of the queue
                    level_vals.append(node.val)          # take the value of the node and copy it to level
                    if node.left:
                        processing_queue.append(node.left)
                    if node.right:
                        processing_queue.append(node.right)
                    processing_queue.pop(0)
                result.append(level_vals)
            return result[::-1]
