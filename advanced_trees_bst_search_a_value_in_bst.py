# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if not A:
            return 0

        while A!=None:
            if A.val==B:
                return 1
            elif A.val >B:
                A=A.left
            else:
                A=A.right
            
        return 0


    

