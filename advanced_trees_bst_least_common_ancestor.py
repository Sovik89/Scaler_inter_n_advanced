# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0
        
        #if both B and C is less than A.val
              
        if B<A.val and C<A.val:
            return self.solve(A.left,B,C)
        #if both B and C is greater than A.val
        if B>A.val and C>A.val:
            return self.solve(A.right,B,C)
        # any other situation yields A.val
        return A.val

