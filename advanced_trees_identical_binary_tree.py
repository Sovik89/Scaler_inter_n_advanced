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
	# @param B : root node of tree
	# @return an integer
    def isSameTree(self, A, B):
               
        #both trees are empty
        if not A and not B:
            return 1
        
        #any of the tree empty
        if not A or not B:
            return 0

        if A.val!=B.val:
            return 0
        
        return self.isSameTree(A.left,B.left) and self.isSameTree(A.right,B.right)
            

        
