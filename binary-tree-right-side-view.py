# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            levelorder = self.levelOrderTraversal(root)
            final_result = []
            l_o_l = len(levelorder)
            for i in xrange(l_o_l):
                final_result.append(levelorder[i][len(levelorder[i])-1])
            return final_result

    def levelOrderTraversal(self,root):
            if root is None:
                return []
            else:
                processing_queue , return_list = [root] , []
                while processing_queue:
                    level_vals = []
                    length = len(processing_queue)
                    for i in xrange(len(processing_queue)):
                        temp_node = processing_queue[0]
                        level_vals.append(temp_node.val)
                        if temp_node.left:
                            processing_queue.append(temp_node.left)
                        if temp_node.right:
                            processing_queue.append(temp_node.right)
                        processing_queue.pop(0)
                    return_list.append(level_vals)
                return return_list


my_solution = Solution()
