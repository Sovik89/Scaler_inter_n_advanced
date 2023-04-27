# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def __init__(self):
        self.prev=None
        self.first=None
        self.second=None
        
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        
        if self.prev and self.prev.val>root.val:
            if not self.first:
                self.first=self.prev
                self.second=root
            else:
                self.second=root
                return
        self.prev=root
        self.inorder(root.right)
            
    # mother function    
    def recoverTree(self, A):
        self.inorder(A)
        
        if not self.first:
            return [-1,-1]
        else:
            self.first,self.second=self.second,self.first
            return [self.first.val,self.second.val]