# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isBST(self, A, start,end):
        if not A:
            return 1
        
        if start <= A.val <=end:
            return self.isBST(A.left,start,A.val-1) and self.isBST(A.right,A.val+1,end)
        
        return 0

    # controlling function
    def isValidBST(self, A):
        is_a_valid_bst=self.isBST(A,-1,float('inf'))#condt 0<=node val<=2^32-1

        return is_a_valid_bst
