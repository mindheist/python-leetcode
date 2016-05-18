# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.root = root

        if self.root is None:
            return None
        else:
            preorder_dict = self.preorder(self.root)
            left_depth = 1
            while self.root.left:
                 self.root = self.root.left
                 left_depth = left_depth + 1
                 print self.root.val
            for i in xrange(len(preorder_dict.keys())-left_depth):
            #while True:
                 self.root.left = preorder_dict[self.root.val]

    def preorder(self,root):
        processing_stack , results = [] , {}
        processing_stack.append(root)
        while processing_stack:
            temp_node = processing_stack.pop()
            results[temp_node.val] = temp_node
            if temp_node.right:
                processing_stack.append(temp_node.right)
            if temp_node.left:
                processing_stack.append(temp_node.left)
        return results
