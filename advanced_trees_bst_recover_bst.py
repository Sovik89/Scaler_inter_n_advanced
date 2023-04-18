# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):
        prev=None
        first=None
        second=None
        
        root=A

        def inorder(root):
            nonlocal prev,first,second
            if root == None:
                return
            
            inorder(root.left)

            if prev and prev.val>root.val:
                if not first:
                    first=prev
                    second=root
                else:
                    second=root
            
                

            prev=root

            inorder(root.right)
        
        inorder(root)

        

        if not first:
            return [-1,-1]
        else:
            first,second=second,first
            return [first.val,second.val]