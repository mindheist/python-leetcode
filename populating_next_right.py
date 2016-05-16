# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        # Basic idea : Do a level order traversal and have a list of list of objects
        # Do another parse and change the third pointer
        final_results = []
        self.root = root
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None :
            pass
        else:
            # do a level order traversal ( this is exactly the same as the previous level order traversal we've done)
            # except that , instead of values - we are appending nodes per level
            processing_queue = []
            processing_queue.append(self.root)
            while processing_queue:
                level_vals,length = [],len(processing_queue)
                for i in range(length):
                    temp_node = processing_queue[0]
                    level_vals.append(temp_node)
                    if temp_node.left:
                        processing_queue.append(temp_node.left)
                    if temp_node.right:
                        processing_queue.append(temp_node.right)
                    processing_queue.pop(0)
                final_results.append(level_vals)


            for i in xrange(len(final_results)):
                if len(final_results[i])==1:
                    continue
                else:
                    for j in xrange(len(final_results[i])-1):
                        final_results[i][j].next = final_results[i][j+1]
