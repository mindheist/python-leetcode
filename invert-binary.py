# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,key):
        self.key = key
        self.items.insert(0,key)

    def dequeue(self):
        return self.items.pop()

    def empty(self):
        return self.items

    def isempty(self):
        return len(self.items)==0

    def print_q(self):
        return self.items

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            my_queue = Queue()
            my_queue.enqueue(root)
            while not my_queue.isempty():
                node = my_queue.dequeue()
                node.left , node.right = node.right , node.left
                if node.left is not None:
                    my_queue.enqueue(node.left)
                if node.right is not None:
                    my_queue.enqueue(node.right)
        return root
