# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isSymmetric(self, A):
        def isMirror(lh,rh):
            
            if lh==None or rh==None:
                return lh==rh
            
            elif (lh.val != rh.val):
                return 0
            
            

            return isMirror(lh.left,rh.right) and isMirror(lh.right,rh.left)

        value = int(isMirror(A,A))

        return value