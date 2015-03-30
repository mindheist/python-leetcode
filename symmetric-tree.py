# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetricHelper(self,left,right):
	    if left == None and right == None :
	    	return True
	    elif left == None or right == None :
	    	return False
	    elif left.val != right.val :
	    	return False
	    else :
	    	return self.isSymmetricHelper(left.right , right.left) and self.isSymmetricHelper(left.left,right.right)
    
    def isSymmetric(self, root):
    	if root == None : return True
    	else:
    		return self.isSymmetricHelper(root.left,root.right)