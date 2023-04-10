# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        max_val=float('-inf')

        if A == None:
            return 0

        left=self.solve(A.left)
        right=self.solve(A.right)

        value=A.val

        return max(value,max(left,right))

        
