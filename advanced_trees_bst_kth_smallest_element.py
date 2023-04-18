# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys
sys.setrecursionlimit(10**6)

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def inorder(self,root,arr):
        if not root:
            return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
    
	def kthsmallest(self, A, B):
        list_val=[]
        self.inorder(A,list_val)

        return list_val[B-1]